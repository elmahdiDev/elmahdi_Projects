
(function(){
  angular.module("hotelreservation.angapp",[])
  .controller("HotelReservation",["$scope",HotelReservation]);
  
  function HotelReservation($scope) {
    $scope.hotels=[
      {hotel_name:"sheraton",hotel_city:"dubai"},
      {hotel_name:"hilton",hotel_city:"amman"},
    ];
    $scope.add_new_hotel=function(new_hotel) {
      var hotel={hotel_name:new_hotel,hotel_city:'city not defined'};
      $scope.hotels.push(hotel);
    };
  }
})();
