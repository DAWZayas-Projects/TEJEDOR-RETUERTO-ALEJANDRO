var app = angular.module("cartelera");

app.controller('FilmsController', ['$scope', '$element', 'FilmsService', function($scope, $element, FilmsService) {
    $scope.movies = [];
    $scope.comingSoon = [];
    FilmsService.getFilms().then(function(data) {
        $scope.movies = data;
    })
    FilmsService.getFutureFilms().then(function(data) {
        $scope.comingSoon = data;
    })
}]);