%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Utility functions %%%
%%%%%%%%%%%%%%%%%%%%%%%%%

% To merge two lists (without duplicates) without adding the duplicates
% merge_without_duplicates(First list, Second list, Merged list)
merge_without_duplicates(ListA, [], ListA).
merge_without_duplicates(ListA, [New|Tail], ListConcat) :- (
    not(member(New, ListA)),
    merge_without_duplicates(ListA, Tail, TailConcat),
    ListConcat=[New|TailConcat]
    ).
merge_without_duplicates(ListA, [New|Tail], ListConcat) :- (
    member(New, ListA),
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