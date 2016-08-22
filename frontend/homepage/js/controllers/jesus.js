(function () {
    'use strict';

    angular
        .module('homepage.avisame.pe')
        .controller('jesusController', jesusController)

    jesusController.$inject = ['$scope'];

    function jesusController() {
        this.mensaje = 'hola jesus pdddddd';
    }
})();