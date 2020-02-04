    const date_picker_element = document.querySelector('.date-picker');
    const selected_date_element = document.querySelector('.date-picker .selected-date');
    const dates_element = document.querySelector('.date-picker .dates');
    const mth_element = document.querySelector('.date-picker .dates .month .mth');
    const next_mth_element = document.querySelector('.date-picker .dates .month .next-mth');
    const prev_mth_element = document.querySelector('.date-picker .dates .month .prev-mth')
    const days_element = document.querySelector('.date-picker .dates .days');
    const months = ['January', 'Febraury', 'March' , 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

    let date = new Date();
    let day = date.getDate();
    let month = date.getMonth();
    let year = date.getFullYear();

    let selectedDate = date;
    let selectedDay = day;
    let selectedMonth = month;
    let selectedYear = year;

    mth_element.textContent = months[months] + '' + year;

    selected_date_element.textContent = format(date); // review format was doing and  the command might be a little different

    populateDate();


    //Event Listener
    date_picker_element.addEventListener('click', toggleDatePicker);
    next_mth_element =  addEventListener('click', goToNextMonth);
    prev_mth_element =  addEventListener('click', goToPrevMonth);


    // functions
    function toggleDatePicker(e){

        if (!checkEventPathForClass(e.path, 'dates'))
        dates_element.classList.toggle('active');
    }

    function goToNextMonth(x){
        month++;
        if (month > 11){
            month = 0;
            year ++;
        }
        mth_element.textContent = month[month] + ' ' + year;
        populateDate();
    }

    function goPrevMonth(x){
        month--;
        if (month > 0){
            month = 11;
            year --;
        }
        mth_element.textContent = month[month] + ' ' + year;
        populateDate(); // ended here at 38:52
    }

    // most important func

    function populateDate(z){
        days_element.innerHTML = '';
        let amount_days = 31;
        if (month == 1){
            amount_days = 28;
        }

        for (let z = 0; z <amount_days; z ++){
            const days_element = document.createElement('div');
            days_element.classList.add('day');
            days_element.textContent = x + 1;

            if(selectedDate == (z+1) && selectedYear == year && selectedMonth == month){
                days_element.classList.add('selected');
            }

            days_element.addEventListener('click', function(){
                selectedDate = new Date(year + '-' + (month +1) + '-' + (z +1));
                selectedDay = (x +1);
                selectedMonth = month;
                selectedYear = year;
                selected_date_element.textContent = formatDate(selectedDate);
                selected_date_element.dataset.value = selectedDate;
                });

            days_element.appendChild(days_element);
        }
    }

    // helper function
    function checkEventPathForClass(path, selector){
        for(let x =0; x< path.length; x++){
            if(path[x].classList && path[x].classList.contains(selector)){
                return true; // doesn't open and close like its supposed to
            }
        }

        return false
    }
    function formatDate(z){
        let day = z.getDate();
        if (day <10){
            day ='0' + day;
        }
        let month = z.getMonth() +1;
        if (month<10) {
            month = '0' + month;
        }

        let year = z.getFullYear();

        return  day + "/" + month + '/' + year;
    }