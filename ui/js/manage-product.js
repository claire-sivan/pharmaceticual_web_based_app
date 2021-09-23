var productModal = $("#productModal");
    $(function () {

        //JSON data by API call
        $.get(productListApiUrl, function (response) {
            if(response) {
                var table = '';
                $.each(response, function(index, product) {
                table += '<tr data-id ="'+ product.product_id +'" data-name="'+ product.name +'" data-stock="'+ product.stock +'" data-price="'+ product.price +'"data-unit="'+ product.dosage_id +'">' +
                        '<td>'+ product.name +'</td>'+
                        '<td>'+ product.stock +'</td>'+
                        '<td>'+ product.price +'</td>'+
                        '<td>'+ product.dosage_name +'</td>'+
                        '<td><span class="btn btn-xs btn-danger delete-product">Delete</span></td></tr>';
                });
                $("table").find('tbody').empty().html(table);
            }
        });
    });


 // Edit Product

    $(document).on("click", ".edit-product", function(){
        var tr = $(this).closest('tr');
        $("#id").val(tr.data)('id');
        $("#name").val(tr.data)('name');
        $("#stock").val(tr.data)('stock');
        $("#price").val(tr.data)('price');
        $("#unit").val(tr.data)('unit');
        productModal.find('.modal-title').text('Edit Product');
        productModal.show('show');
     });
        

    // Save Product
    $("#saveProduct").on("click", function () {
        // If we found id value in form then update product detail
        var data = $("#productForm").serializeArray();
        var requestPayload = {
            product_name: null,
            stock: null,
            price: null,
            dosage_id: null
        };
        for (var i=0;i<data.length;++i) {
            var element = data[i];
            switch(element.name) {
                case 'name':
                    requestPayload.product_name = element.value;
                    break;
                case 'stock':
                    requestPayload.stock = element.value;
                    break;
               case 'price':
                    requestPayload.price = element.value;
                    break;
                case 'dosages':
                    requestPayload.dosage_id = element.value;
                    break;
            }
        }
        callApi("POST", productSaveApiUrl, {
            'data': JSON.stringify(requestPayload)
        });
    });

    $(document).on("click", ".delete-product", function (){
        var tr = $(this).closest('tr');
        var data = {
            product_id : tr.data('id')
        };
        var isDelete = confirm("Are you sure to delete "+ tr.data('name') +" item?");
        if (isDelete) {
            callApi("POST", productDeleteApiUrl, data);
        }
    });

    productModal.on('hide.bs.modal', function(){
        $("#id").val('0');
        $("#name, #stock, #price, #unit").val('');
        productModal.find('.modal-title').text('Add New Product');
    });

    productModal.on('show.bs.modal', function(){
        //JSON data by API call
        $.get(dosageListApiUrl, function (response) {
            if(response) {
                var options = '<option value="">--Select--</option>';
                $.each(response, function(index, dosage) {
                    options += '<option value="'+ dosage.dosage_id +'">'+ dosage.dosage_name +'</option>';
                });
                $("#dosages").empty().html(options);
            }
        });
    });