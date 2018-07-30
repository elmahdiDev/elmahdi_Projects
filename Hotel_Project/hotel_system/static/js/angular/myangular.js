
(function(){
  angular.module("hotelreservation.angapp",[])
  .controller("HotelReservation",["$scope","$http",HotelReservation])
  .controller("Customers",["$scope","$http",Customers])
  .controller("Reservations",["$scope","$http",Reservations]);

  
  function HotelReservation($scope,$http) {
    reload_data();
    function reload_data(){
      $scope.hotels=[];
      $http.get("/reservation/hotelsapi/")
      .then(function(response){
        $scope.hotels = response.data;
      });
    }

    $scope.delete_hotel=function(id){
      $http.delete("/reservation/hotelsapi/"+id+"/")
      .then(function(){
        reload_data();
      }, function(){
        alert('error  while deleting the hotel')
      });
    }
   
    $scope.add_new_hotel=function(hotelname,city,totalrooms,emptyrooms) {
      var hotel={hotel_name:hotelname,hotel_city:city,total_rooms:totalrooms,empty_rooms:emptyrooms};
      $http.post("/reservation/hotelsapi/",hotel)
      .then(function(response){
        $scope.hotels.push(hotel);
      },function(){//Error
        alert('error while adding hotel');
      });
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
  $scope.add_new_reservation=function(hotelname,customername,starttime,endtime) {
    var reservation={hotel:hotelname,customer:customername,start_time:starttime,end_time:endtime};
    $scope.reservations.push(reservation);
  };
}


})();

