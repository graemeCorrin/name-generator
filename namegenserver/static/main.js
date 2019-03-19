(function () {

  'use strict';

  angular.module('NameGeneratorApp', [])

  .controller('NameGeneratorController', ['$scope', '$log', '$http', '$timeout',
    function($scope, $log, $http, $timeout) {

    $scope.getName = function() {

      $log.log("test");

      var seed = $scope.seed;

      // fire the API request
      $http.post('/name', {'seed': seed}).
        success(function(results) {
          $log.log(results);
          if ($scope.names) {
            $scope.names = {...$scope.names, ...results};
          }else{
            $scope.names = results;
          }


        }).
        error(function(error) {
          $log.log(error);
        });

    }

    $scope.clear = function() {

      $log.log("test");
      $scope.names = null;

    };
  }
  ]);

}());

