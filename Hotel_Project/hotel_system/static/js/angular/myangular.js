
(function(){
  angular.module("hotelreservation.angapp",[])
  .controller("HotelReservation",["$scope","$http",HotelReservation])
  .controller("Customers",["$scope","$http",Customers])
  .controller("Reservations",["$scope","$http",Reservations]);

  
  function HotelReservation($scope,$http) {
    $scope.hotels=[];
    $http.get("/reservation/hotelsapi/")
    .then(function(response){
      $scope.hotels = response.data;
    });
    $scope.add_new_hotel=function(new_hotel) {
      var hotel={hotel_name:new_hotel,hotel_city:'city not defined'};
      $scope.hotels.push(hotel);
    };
  }



function Customers($scope,$http) {
  $scope.customers=[];
  $http.get("/reservation/customersapi/")
  .then(function(response){
    $scope.customers = response.data;
  });
  $scope.add_new_customer=function(new_customer) {
    var customer={customer_name:new_customer,customer_number:'987546848'};
    $scope.customers.push(customer);
  };
}




function Reservations($scope,$http) {
  $scope.reservations=[];
  $http.get("/reservation/reservationsapi/")
  .then(function(response){
    $scope.reservations = response.data;
  });
  $scope.add_new_reservation=function(hotelname,customername,start_time,end_time) {
    var reservation={hotel:hotelname,customer:customername,starttime:start_time,endtime:end_time};
    $scope.reservations.push(reservation);
  };
}


})();

