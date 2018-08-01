
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

    $scope.update_hotel=function(id,hotelname,city,totalrooms,emptyrooms){
      var hotelupdate={hotel_name:hotelname,hotel_city:city,total_rooms:totalrooms,empty_rooms:emptyrooms};
      $http.put("/reservation/hotelsapi/"+id+"/",hotelupdate)
      .then(function(){
        reload_data();
      }, function(){
        alert('Error while updating hotel info')
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
  reload_customers()
  function reload_customers(){
    $scope.customers=[];
    $http.get("/reservation/customersapi/")
    .then(function(response){
      $scope.customers = response.data;
    });
  }
  $scope.add_new_customer=function(new_customer) {
    var customer={customer_name:new_customer,customer_number:'987546848'};
    $http.post("/reservation/customersapi/",customer)
      .then(function(response){
        $scope.customers.push(customer);
      },function(){//Error
        alert('error while adding customer');
      });
  }

  $scope.delete_customer=function(id){
    $http.delete("/reservation/customersapi/"+id+"/")
    .then(function(){
      reload_customers();
    }, function(){
      alert('error  while deleting the customer')
    });
  }

  $scope.update_customer=function(id,updatecustomer){
    var customerupdate={customer_name:updatecustomer,customer_number:'987546848'};
    $http.put("/reservation/customersapi/"+id+"/",customerupdate)
    .then(function(){
      reload_customers();
    }, function(){
      alert('Error while updating customer info')
    });
  }
}




function Reservations($scope,$http) {
  reload_reservations()
  function reload_reservations(){
    $scope.reservations=[];
    $http.get("/reservation/reservationsapi/")
    .then(function(response){
      $scope.reservations = response.data;
    });
  }
  $scope.add_new_reservation=function(hotelname,customername) {
    var reservation={hotel:hotelname,customer:customername,start_time:"2018-09-13T13:04:00Z",end_time:"2018-09-13T13:04:00Z"};
    $http.post("/reservation/reservationsapi/",reservation)
      .then(function(response){
        $scope.reservations.push(reservation);
      },function(){//Error
        alert('error while adding new reservation');
      });
  };

  $scope.delete_reservation=function(id){
    $http.delete("/reservation/reservationsapi/"+id+"/")
    .then(function(){
      reload_reservations();
    }, function(){
      alert('error  while deleting the reservation')
    });
  }

  $scope.update_reservation=function(id,updatedhotel,update_customer){
    var reservationupdate={hotel:updatedhotel,customer:updatedcustomer,start_time:"2018-09-13T13:04:00Z",end_time:"2018-09-13T13:04:00Z"};
    $http.put("/reservation/reservationsapi/"+id+"/",reservationupdate)
    .then(function(){
      reload_reservations();
    }, function(){
      alert('Error while updating reservation info')
    });
  }
}


})();

