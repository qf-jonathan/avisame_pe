(function () {
    angular
        .module('homepage.avisame.pe')
        .controller('mainController', mainController);

    mainController.$inject = ['$scope'];

    function mainController($scope) {
        var vm = this;
        vm.mensaje = "hola mundo";
    }
})();
