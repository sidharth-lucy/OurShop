$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function(){
    var id = $(this).attr("productId").toString();
    // console.log(id)
    var eml = this.parentNode.children[2];
    $.ajax({
        type:'GET',
        url:'/pluscart',
        data:{
            prod_id: id
        },

        success: function(data){
            // console.log(data);
            eml.innerText= data.quantity;
            document.getElementById('amount').innerText = data.amount;
            document.getElementById('sip-charge').innerText = data.shipping_charge;
            document.getElementById('totalcost').innerText = data.total_cost;
        }
    })
})



$('.minus-cart').click(function(){
    var id = $(this).attr('productId').toString();
    // console.log(id);
    var emll = this.parentNode.children[2];

    $.ajax({
        type: 'GET',
        url: '/minuscart',
        data:{
            prod_id:id,
        },

        success: function(data){
            // console.log(data);
            emll.innerText = data.quantity;
            document.getElementById('amount').innerText = data.amount;
            // $('#amount').innerText = data.amount;
            // $('#sip-charge').innerText = data.shipping_charge;
            document.getElementById('sip-charge').innerText = data.shipping_charge;
            // $('#totalcost').innerText = data.total_cost;
            document.getElementById('totalcost').innerText = data.total_cost;
            
        }

    })


})


$('.removeitem').click(function(){
    var prod_id = $(this).attr('productId');
    // console.log(prod_id);
    var elm = this ;
    $.ajax({
        type: 'GET',
        url: '/removecart-item',
        data:{
            'prod_id':prod_id
        },
        success: function(data){
            // console.log(data);

            document.getElementById('amount').innerText = data.amount;
            document.getElementById('totalcost').innerText = data.total_cost;
            document.getElementById('sip-charge').innerText = data.shipping_charge;
            elm.parentNode.parentNode.parentNode.parentNode.remove() ;
        }

    })

})

