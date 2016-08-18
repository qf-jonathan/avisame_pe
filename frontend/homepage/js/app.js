(function () {
    'use strict';
    
    angular
        .module('homepage.avisame.pe', [
            'ngRoute'
        ])
        .config(config);

    function config($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: '/static/homepage/templates/main-template.html',
                controller: 'mainController',
                controllerAs: 'vm'
            })
            .when('/test', {
                templateUrl: '/static/homepage/templates/test-template.html'
            });
    }
})();
