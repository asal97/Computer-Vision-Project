var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
    // This function will display the specified tab of the form...
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    //... and fix the Previous/Next buttons:
    if (n == 0) {
        document.getElementById("prevBtn").style.display = "none";
    } else {
        document.getElementById("prevBtn").style.display = "inline";
    }
    if (n == (x.length - 1)) {
        document.getElementById("nextBtn").innerHTML = "ثبت";
    } else {
        document.getElementById("nextBtn").innerHTML = "بخش بعدی";
    }
    //... and run a function that will display the correct step indicator:
    fixStepIndicator(n)
}

function nextPrev(n) {
    // This function will figure out which tab to display
    var x = document.getElementsByClassName("tab");
    // Exit the function if any field in the current tab is invalid:
    if (n == 1 && !validateForm()) return false;
    // Hide the current tab:
    x[currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    currentTab = currentTab + n;
    // if you have reached the end of the form...
    if (currentTab >= x.length) {
        // ... the form gets submitted:
        document.getElementById("register-form").submit();
        return false;
    }
    // Otherwise, display the correct tab:
    showTab(currentTab);
}

function validateMelliCode(melliCode) {

    if (melliCode.length != 10) {
        return false; // Melli Code is less or more than 10 digits
    } else {
        var sum = 0;

        for (var i = 0; i < 9; i++) {
            sum += parseInt(melliCode.charAt(i)) * (10 - i);
        }

        var lastDigit;
        var divideRemaining = sum % 11;

        if (divideRemaining < 2) {
            lastDigit = divideRemaining;
        } else {
            lastDigit = 11 - (divideRemaining);
        }

        if (parseInt(melliCode.charAt(9)) == lastDigit) {
            return true;
        } else {
            return false; // Invalid MelliCode
        }
    }
}

function validateForm() {
    var form = document.forms["multiPageForm"];
    var message = "دقت کنید حتما بخش های ضروری را پر کرده باشید";
    var valid = true;
    switch (currentTab) {
        case 1: // مشخصات ماشین
        {
            if (document.getElementById("id_plate_type").value == "2") { // سواری انزلی
                if(form["plate_firstnum"].value.length != 5){
                    message = "بخش اول پلاک باید ۵ رقمی باشد";
                    valid = false;
                }
                else if(form["plate_secondnum"].value.length != 2){
                    message = "بخش دوم پلاک باید ۲ رقمی باشد";
                    valid = false;
                }
            } else { // پلاک ملی
                if(form["plate_firstnum"].value.length != 2){
                    message = "بخش اول پلاک باید ۲ رقمی باشد";
                    valid = false;
                } else if(form["plate_secondnum"].value.length != 3){
                    message = "بخش دوم پلاک باید ۳ رقمی باشد";
                    valid = false;
                } else if(form["plate_citynum"].value.length != 2){
                    message = "کد شهرستان باید ۲ رقمی باشد";
                    valid = false;
                }
            }
            break;
        }
        case 2: // مشخصات ظاهری
        {
            if (form["vehicle_color"].value.length && form["vehicle_type"].value.length &&
                form["vehicle_picture"].value.length) {

            } else {
                valid = false;
            }
            break;
        }
        default: // مشخصات مالک
        {
            if (document.getElementById("owner_select").value == "old_owner") { // از مالکین ثبت شده در سیستم
                if (!validateMelliCode(form["owner_nationalcode"].value)) {
                    message = "کد ملی وارد شده معتبر نمی باشد";
                    valid = false;
                }
            } else { // ثبت مالک جدید
                if (form["owner_firstname"].value.length && form["owner_lastname"].value.length &&
                    form["owner_nationalcode"].value.length && form["owner_phone"].value.length &&
                    form["owner_picture"].value.length) {
                    if (!validateMelliCode(form["owner_nationalcode"].value)) {
                        message = "کد ملی وارد شده معتبر نمی باشد";
                        valid = false;
                    } else if (form["owner_phone"].value.length < 10) {
                        message = "تعداد ارقام شماره تماس وارد شده را چک کنید";
                        valid = false;
                    }
                } else {
                    valid = false;
                }
            }
        }
    }
    if (!valid) {
        alert(message);
    }
    return valid;
}

function fixStepIndicator(n) {
    // This function removes the "active" class of all steps...
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    //... and adds the "active" class on the current step:
    x[n].className += " active";
}