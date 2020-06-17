$("#owner_select").change(function () {
    if ($(this).val() == "old_owner") {
        //      $("#tab-first").addClass('has-success').removeClass('has-error');
        // $('#owner_nationalcode_div').classList = 'col-lg-12 col-md-12 col-sm-12 col-xs-12';
        $('#owner_lastname_div').hide();
        $('#owner_firstname_div').hide();
        $('#owner_phone_div').hide();
        $('#owner_description_div').hide();
        $('#owner_picture_div').hide();
        $('#id_owner_picture').hide();
        // $('#otherField').attr('required', '');
        // $('#otherField').attr('data-error', 'This field is required.');
    } else {
        // $('#owner_nationalcode_div').classList = 'col-lg-6 col-md-6 col-sm-6 col-xs-12';
        $('#owner_lastname_div').show();
        $('#owner_firstname_div').show();
        $('#owner_phone_div').show();
        $('#owner_description_div').show();
        $('#owner_picture_div').show();
        $('#id_owner_picture').show();
        // $('#otherField').removeAttr('required');
        // $('#otherField').removeAttr('data-error');
    }
});
$("#owner_select").trigger("change");

// ----------------------------<PLATE>-----------------------------------------

$("#id_plate_type").change(function () {
    if ($(this).val() == "1") { // سواری ملی
        $('#plate_alpha_div').show();
        $('#plate_citynum_div').show();

        $('#plate_firstnum_id').attr('placeholder', '۹۹');
        $('#plate_secondnum_id').attr('placeholder', '۹۹۹');

        //      $("#tab-first").addClass('has-success').removeClass('has-error');

        // $('#otherField').attr('required', '');
        // $('#otherField').attr('data-error', 'This field is required.');
    } else { // سواری منطقه آزاد انزلی
        $('#plate_alpha_div').hide();
        $('#plate_citynum_div').hide();

        $('#plate_firstnum_id').attr('placeholder', '۹۹۹۹۹');
        $('#plate_secondnum_id').attr('placeholder', '۹۹');
        // $('#otherField').removeAttr('required');
        // $('#otherField').removeAttr('data-error');
    }
});
$("#id_plate_type").trigger("change");

// $("#seeAnotherFieldGroup").change(function () {
//     if ($(this).val() == "yes") {
//         $('#otherFieldGroupDiv').show();
//         $('#otherField1').attr('required', '');
//         $('#otherField1').attr('data-error', 'This field is required.');
//         $('#otherField2').attr('required', '');
//         $('#otherField2').attr('data-error', 'This field is required.');
//     } else {
//         $('#otherFieldGroupDiv').hide();
//         $('#otherField1').removeAttr('required');
//         $('#otherField1').removeAttr('data-error');
//         $('#otherField2').removeAttr('required');
//         $('#otherField2').removeAttr('data-error');
//     }
// });
// $("#seeAnotherFieldGroup").trigger("change");
		