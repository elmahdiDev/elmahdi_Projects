
(function(){
  angular.module("hotelreservation.angapp",[])
  .controller("HotelReservation",["$scope","$http",HotelReservation]);
  
  function HotelReservation($scope,$http) {
    $scope.hotels=[];
    $http.get("/reservation/hotelsapi")
    .then(function(response){
      $scope.hotels = response.data;
    });
    $scope.add_new_hotel=function(new_hotel) {
      var hotel={hotel_name:new_hotel,hotel_city:'city not defined'};
      $scope.hotels.push(hotel);
    };
  }
})();
