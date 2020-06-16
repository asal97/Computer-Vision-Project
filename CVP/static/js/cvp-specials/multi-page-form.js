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

function validateForm() {
    var form = document.forms["multiPageForm"];
    var message = "دقت کنید حتما بخش های ضروری را پر کرده باشید";
    var valid = true;
    switch (currentTab) {
        case 1: // مشخصات ماشین
        {
            if (form["plate_firstnum"].value.length && form["plate_secondnum"].value.length &&
                form["plate_citynum"].value.length) {

            } else {
                valid = false;
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
            if (form["owner_firstname"].value.length && form["owner_lastname"].value.length &&
                form["owner_nationalcode"].value.length && form["owner_phone"].value.length &&
                form["owner_picture"].value.length) {
                break;
            } else {
                valid = false;
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