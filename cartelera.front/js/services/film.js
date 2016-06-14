app.factory('FilmsService', ['AppConfig', '$http', '$q', function(AppConfig, $http, $q) {
    var service = {};
    service.getFilms = function(options) {
        var defer = $q.defer();
        var url = AppConfig.generateURL('/films/');
        var uri = new URI(url);

        $http.get(uri.toString()).success(function(data) {
            defer.resolve(data);
        });

        return defer.promise;
    };
    service.getFutureFilms = function(options) {
        var defer = $q.defer();
        var url = AppConfig.generateURL('/comingSoon/');
        var uri = new URI(url);
        $http.get(uri.toString()).success(function(data) {
            defer.resolve(data);
        });

        return defer.promise;
    };

    return service;
}]);