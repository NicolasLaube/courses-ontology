%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Utility functions %%%
%%%%%%%%%%%%%%%%%%%%%%%%%

% To merge two lists (without duplicates) without adding the duplicates
% merge_without_duplicates(First list, Second list, Merged list)
merge_without_duplicates(ListA, [], ListA).
merge_without_duplicates(ListA, [New|Tail], ListConcat) :- (
    not(member(New, ListA)),
    !,
    merge_without_duplicates(ListA, Tail, TailConcat),
    ListConcat=[New|TailConcat]
    ).
merge_without_duplicates(ListA, [_|Tail], ListConcat) :- (
    merge_without_duplicates(ListA, Tail, ListConcat)
    ).

% To filter out some elements from a list
% filter_list(List to filter, Elements to delete, Filtered list)
filter_list([], _, []).
filter_list([Y|Tail], ToDelete, NewFilteredList) :- (
    member(Y, ToDelete),
    !,
    filter_list(Tail, ToDelete, NewFilteredList)
    ).
filter_list([Y|Tail], ToDelete, NewFilteredList) :- (
    filter_list(Tail, ToDelete, FilteredList),
    NewFilteredList=[Y|FilteredList]
    ).

% To merge 2 dictionaries
% merge_dict(First dict, Second dict, Merged dict)
merge_dict(Dict1, dict{}, Dict1).
merge_dict(Dict1, Dict2, NewDictMerged) :- (
    X=Dict2.get(K),
    not(_=Dict1.get(K)),
    !,
    del_dict(K, Dict2, _, Dict2Filtered),
    merge_dict(Dict1, Dict2Filtered, DictMerged),
    NewDictMerged=DictMerged.put(K,X)
    ).
merge_dict(Dict1, Dict2, NewDictMerged) :- (
    _=Dict2.get(K),
    !,
    del_dict(K, Dict2, _, Dict2Filtered),
    merge_dict(Dict1, Dict2Filtered, NewDictMerged)
    ).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Dependency getter functions %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Get direct dependencies %%

% To find all the directly requested modules for studying a new module
% find_req_modules(New module, Temporary list (should be empty), Requested module)
find_req_modules(X, Tmp, List):-
    (
        module(X),
        requires_module(X, New),
        not(member(New, Tmp)) ->
        find_req_modules(X, [New|Tmp], List); List = Tmp 
    ).

% To find all the directly requested modules in a specific course for studying a new module
% find_req_modules(New module, Course, Temporary list (should be empty), Requested module)
find_req_modules_with_course(X, C, Tmp, List):-
    (
        module(X),
        course(C),
        requires_module(X, New),
        has_as_module(C, New),
        not(member(New, Tmp)) ->
        find_req_modules_with_course(X, C, [New|Tmp], List); List = Tmp 
    ).

% To find all the modules in a specific course
% find_course_modules(Course, Temporary list (should be empty), Modules in Course)
find_course_modules(C, Tmp, List):-
    (
        course(C),
        has_as_module(C, New),
        not(member(New, Tmp)) ->
        find_course_modules(C, [New|Tmp], List); List = Tmp 
    ).

% To find two modules in a course, one being required by the other
% requires_module_in_course(First module, Course, Module required by the first one)
requires_module_in_course(X, C, Y) :- (
    requires_module(X, Y),
    has_as_module(C, X),
    has_as_module(C, Y)
    ).

% To find the minimum number of modules in a course such that all modules if this course are required by them
% find_independant_course_modules(Course, Temporary list (should be empty), Modules associated with this Course)
find_independant_course_modules(C, Tmp, IndependantModules) :-
    (
        course(C),
        has_as_module(C, New),
        not(requires_module_in_course(_, C, New)),
        not(member(New, Tmp)) ->
        find_independant_course_modules(C, [New|Tmp], IndependantModules); IndependantModules = Tmp 
    ).

% To find all the directly requested modules in a specific course for studying a list of modules
% get_dependencies_from_list(New modules, Course, Dependencies)
get_dependencies_from_list([], C, []) :- course(C).
get_dependencies_from_list([X|Tail], C, Dependencies) :- (
    course(C),
    module(X),
    get_all_dependencies(X, C, DependenciesX),
    get_dependencies_from_list(Tail, C, DependenciesTail),
    merge_without_duplicates(DependenciesTail, DependenciesX, Dependencies)
    ).

%% Get all dependencies %%

% To get all dependencies for studying a module in a specific course
% get_all_dependencies_from_list(Module to study, 
%                                Course, 
%                                Modules to check for new dependencies, 
%                                Modules that were already visited and should never be again (higher level), 
%                                Modules that were already visited so we don't want to visit them another time (lower level), 
%                                Dependencies that are currently found)
get_all_dependencies_from_list(X, C, [], _, _, []) :- (
    module(X),
    course(C)
    ).
get_all_dependencies_from_list(X, C, _, AlreadyVisited, _, _) :- (
    module(X),
    course(C),
    member(X, AlreadyVisited),
    write(X),
    write(" has a circular dependency"),
    halt
    ).
get_all_dependencies_from_list(X, C, [Y|Tail], AlreadyVisited, AlreadySearched, NewDependencies) :- (
    module(X),
    course(C),
    module(Y),
    not(member(Y, AlreadySearched)),
    get_all_dependencies_from_list(X, C, Tail, AlreadyVisited, AlreadySearched, DependenciesTail),
    merge_without_duplicates(AlreadySearched, DependenciesTail, NewAlreadySearched),
    find_req_modules_with_course(Y, C, [], DepY),
    get_all_dependencies_from_list(Y, C, DepY, [X|AlreadyVisited], NewAlreadySearched, DependenciesY),
    merge_without_duplicates(DependenciesTail, DependenciesY, Dependencies),
    NewDependencies=[Y|Dependencies]
    ).
get_all_dependencies_from_list(X, C, [Y|Tail], AlreadyVisited, AlreadySearched, NewDependencies) :- (
    module(X),
    course(C),
    module(Y),
    member(Y, AlreadySearched),
    get_all_dependencies_from_list(X, C, Tail, AlreadyVisited, AlreadySearched, DependenciesTail),
    NewDependencies=[Y|DependenciesTail]
    ).

% Overlay: To get all dependencies for studying a module in a specific course
% get_all_dependencies(Module to study, Course, Dependencies associated with the module)
get_all_dependencies(X, C, Dependencies) :- (
    find_req_modules_with_course(X, C, [], DepX),
    get_all_dependencies_from_list(X, C, DepX, [], [], Dependencies)
    ).

% To get all dependencies until a specified graph level
% get_all_dependencies_until_level_with_list(Module to study, 
%                                            Course, 
%                                            Min graph level, 
%                                            Modules to check for new dependencies, 
%                                            Modules that were already visited and should never be again (higher level), 
%                                            Modules that were already visited so we don't want to visit them another time (lower level), 
%                                            Modules associated with their level, 
%                                            Dependencies that are currently found).

get_all_dependencies_until_level_with_list(X, C, _, [], _, _, _, []) :- (
    module(X),
    course(C)
    ).
get_all_dependencies_until_level_with_list(X, C, MinLevel, _, _, _, AllLevels, []) :- (
    module(X),
    course(C),
    LevelX=AllLevels.get(X),
    LevelX =:= MinLevel,
    !
    ).
get_all_dependencies_until_level_with_list(X, C, _, _, AlreadyVisited, _, _, _) :- (
    module(X),
    course(C),
    member(X, AlreadyVisited),
    write(X),
    write(" has a circular dependency"),
    halt
    ).
get_all_dependencies_until_level_with_list(X, C, MinLevel, [Y|Tail], AlreadyVisited, AlreadySearched, AllLevels, NewDependencies) :- (
    module(X),
    course(C),
    module(Y),
    not(member(Y, AlreadySearched)),
    !,
    get_all_dependencies_until_level_with_list(X, C, MinLevel, Tail, AlreadyVisited, AlreadySearched, AllLevels, DependenciesTail),
    merge_without_duplicates(AlreadySearched, DependenciesTail, NewAlreadySearched),
    find_req_modules_with_course(Y, C, [], DepY),
    get_all_dependencies_until_level_with_list(Y, C, MinLevel, DepY, [X|AlreadyVisited], NewAlreadySearched, AllLevels, DependenciesY),
    merge_without_duplicates(DependenciesTail, DependenciesY, Dependencies),
    NewDependencies=[Y|Dependencies]
    ).
get_all_dependencies_until_level_with_list(X, C, MinLevel, [Y|Tail], AlreadyVisited, AlreadySearched, AllLevels, NewDependencies) :- (
    module(X),
    course(C),
    module(Y),
    get_all_dependencies_until_level_with_list(X, C, MinLevel, Tail, AlreadyVisited, AlreadySearched, AllLevels, DependenciesTail),
    NewDependencies=[Y|DependenciesTail]
    ).

% Overlay: To get all dependencies until specified graph level for studying a module in a specific course
% get_all_dependencies(Module to study, Course, Min graph level, Modules associated with their level, Dependencies associated with the module)
get_all_dependencies_until_level(X, C, MinLevel, AllLevels, Dependencies) :- (
    module(X),
    course(C),
    find_req_modules_with_course(X, C, [], DepX),
    get_all_dependencies_until_level_with_list(X, C, MinLevel, DepX, [], [], AllLevels, Dependencies)
    ).

% To get all dependencies until specified graph level for a list of modules in a specific course
% get_dependencies_until_level_from_list(List of modules, Course, Min graph level, Modules associated with their level, Dependencies associated with the modules)
get_dependencies_until_level_from_list([], C, _, _, []) :- course(C).
get_dependencies_until_level_from_list([X|Tail], C, MinLevel, AllLevels, Dependencies) :- (
    course(C),
    module(X),
    get_all_dependencies_until_level(X, C, MinLevel, AllLevels, DependenciesX),
    get_dependencies_until_level_from_list(Tail, C, MinLevel, AllLevels, DependenciesTail),
    merge_without_duplicates(DependenciesTail, DependenciesX, Dependencies)
    ).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Functions to build the graph %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Graph level %%

% To find the graph level of a specific module in a specific course
% module_level_in_course_from_req(Module, Course, Modules to inspect (should be empty), Current graph level)
module_level_in_course_from_req(X, _, [], 0) :- module(X).
module_level_in_course_from_req(X, C, [Y|Tail], N) :- (
    module(X),
    module(Y),
    find_req_modules_with_course(Y, C, [], Req_Y),
    module_level_in_course_from_req(Y, C, Req_Y, M),
    module_level_in_course_from_req(X, C, Tail, Mp),
    N is max(M+1,Mp)
    ).

% Overlay: To find the graph level of a specific module in a specific course
% module_level_in_course(Module, Course, Graph level)
module_level_in_course(X, C, N) :- (
    find_req_modules_with_course(X, C, [], Req_X), 
    module_level_in_course_from_req(X, C, Req_X, N)
    ).

% To get the min level of a list of modules
% get_min_level_from_list(List of modules, Modules associated with their level, Min level for the list of modules)
get_min_level_from_list([], _, 0).
get_min_level_from_list([X], AllLevels, MinLevel) :- (
    MinLevel=AllLevels.get(X),
    !
    ).
get_min_level_from_list([Y|Tail], AllLevels, MinLevel) :- (
    LevelY=AllLevels.get(Y),
    get_min_level_from_list(Tail, AllLevels, MinLevelTail),
    MinLevel is min(LevelY, MinLevelTail)
    ).

% To get all the levels of a module and its dependencies in a specific course
% get_all_level_with_dict(Module, Course, Modules to check, Levels of modules already checked, Levels of Module and Modules to check)
get_all_level_with_dict(X, _, [], _, dict{}.put(X, 0)) :- module(X).
get_all_level_with_dict(X, C, [Y|Tail], AlreadyBuiltDict, NewDictLevel) :- (
    module(X),
    course(C),
    module(Y),
    NY=AlreadyBuiltDict.get(Y),
    !,
    get_all_level_with_dict(X, C, Tail, AlreadyBuiltDict, DictLevelTail),
    NTail=DictLevelTail.get(X),
    N is max(NY+1,NTail),
    put_dict(X, DictLevelTail, N, NewDictLevel)
    ).
get_all_level_with_dict(X, C, [Y|Tail], AlreadyBuiltDict, NewDictLevel) :- (
    module(X),
    course(C),
    module(Y),
    find_req_modules_with_course(Y, C, [], Req_Y),
    get_all_level_with_dict(Y, C, Req_Y, AlreadyBuiltDict, DictLevelY),
    NY=DictLevelY.get(Y),
    merge_dict(AlreadyBuiltDict, DictLevelY, NewAlreadyBuiltDict),
    get_all_level_with_dict(X, C, Tail, NewAlreadyBuiltDict, DictLevelTail),
    NTail=DictLevelTail.get(X),
    merge_dict(DictLevelTail, DictLevelY, DictLevel),
    N is max(NY+1,NTail),
    put_dict(X, DictLevel, N, NewDictLevel)
    ).

% Overlay: To get all the levels of a module and its dependencies in a specific course
% get_all_levels(Module, Course, Levels of Module and its dependencies)
get_all_levels(X, C, AllLevels) :- (
    module(X),
    course(C),
    find_req_modules_with_course(X, C, [], Req_X),
    get_all_level_with_dict(X, C, Req_X, dict{}, AllLevels)
    ).

% To get the graph levels of all the modules in a course
% get_all_levels_from_list_in_course(List of modules in course, Course, Levels of modules already checked, Levels of the list of modules)
get_all_levels_from_list_in_course([], C, _, dict{}) :- course(C).
get_all_levels_from_list_in_course([X|Tail], C, AlreadyBuiltDict, NewDictLevel) :- (
    module(X),
    course(C),
    _=AlreadyBuiltDict.get(X),
    !,
    get_all_levels_from_list_in_course(Tail, C, AlreadyBuiltDict, NewDictLevel)

).
get_all_levels_from_list_in_course([X|Tail], C, AlreadyBuiltDict, NewDictLevel) :- (
    module(X),
    course(C),
    find_req_modules_with_course(X, C, [], Req_X),
    get_all_level_with_dict(X, C, Req_X, AlreadyBuiltDict, DictLevelX),
    merge_dict(AlreadyBuiltDict, DictLevelX, NewAlreadyBuiltDict),
    get_all_levels_from_list_in_course(Tail, C, NewAlreadyBuiltDict, DictLevelTail),
    merge_dict(DictLevelTail, DictLevelX, NewDictLevel)
    ).

% Overlay: To get the graph levels of all the modules in a course
% get_all_levels_for_course(Course, Levels of all the modules in the Course)
get_all_levels_for_course(C, AllLevels) :- (
    course(C),
    find_course_modules(C, [], AllModules),
    get_all_levels_from_list_in_course(AllModules, C, dict{}, AllLevels)
).

%% Min dependencies %%

% To get the minimal number of dependencies for a specific module in a specific course
% min_dependencies(Module, Course, Smallest list of dependencies)
get_min_dependencies(X, C, MinDependencies) :- (
    module(X),
    course(C),
    find_req_modules_with_course(X, C, [], RequiredX),
    get_dependencies_from_list(RequiredX, C, AllDependencies),
    filter_list(RequiredX, AllDependencies, MinDependencies)
    ).

% To get the minimal number of dependencies for a specific module in a specific course, knowing the graph levels of the modules
% get_min_dependencies_optimized(Module, Course, Modules associated with their level, Smallest list of dependencies)
get_min_dependencies_optimized(X, C, AllLevels, MinDependencies) :- (
    module(X),
    course(C),
    find_req_modules_with_course(X, C, [], RequiredX),
    get_min_level_from_list(RequiredX, AllLevels, MinLevel),
    get_dependencies_until_level_from_list(RequiredX, C, MinLevel, AllLevels, AllDependencies),
    filter_list(RequiredX, AllDependencies, MinDependencies)
    ).

% To get the minimal number of dependencies for a list of module in a specific course, knowing the graph levels of the modules
% get_min_dependencies_for_list_in_course(List of modules, Course, Modules associated with their level, Smallest list of dependencies for each module)
get_min_dependencies_for_list_in_course([], C, _, dict{}) :- course(C).
get_min_dependencies_for_list_in_course([X|Tail], C, AllLevels, NewMinDependencies) :- (
    course(C),
    module(X),
    get_min_dependencies_for_list_in_course(Tail, C, AllLevels, MinDependenciesTail),
    get_min_dependencies_optimized(X, C, AllLevels, MinDependenciesX),
    put_dict(X, MinDependenciesTail, MinDependenciesX, NewMinDependencies)
    ).

% To get the minimal number of dependencies for a all the modules of a course
% get_min_dependencies_in_course(Course, Smallest list of dependencies for each module)
get_min_dependencies_in_course(C, MinDependencies) :- (
    course(C),
    find_course_modules(C, [], CourseModules),
    get_all_levels_for_course(C, AllLevels),
    get_min_dependencies_for_list_in_course(CourseModules, C, AllLevels, MinDependencies)
    ).