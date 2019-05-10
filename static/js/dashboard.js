var currHours = new Date().getHours()
var update = document.querySelector('button.is-link');
var table = document.getElementById('slots')
var selects = []

if (currHours < 12) {
  document.querySelector('.timeDay').textContent = "Morning"
} else if (currHours < 18) {
  document.querySelector('.timeDay').textContent = "Afternoon"
} else {
  document.querySelector('.timeDay').textContent = "Evening"
};

update.addEventListener('click', function(event) {
    update.classList.add('is-loading');
    for (var i = 1, row; row = table.rows[i]; i++) { // i = 1 instead of 0 to not count the first row aka timings
    // iterate through rows
    // rows would be accessed using the "row" variable assigned in the for loop
        for (var j = 1, col; col = row.cells[j]; j++) { // i = 1 instead of 0 to not count the first col aka names
        // iterate through columns
        // columns would be accessed using the "col" variable assigned in the for loop
            if (table.rows[i].cells[j].classList.contains('is-booked')) {
                selects.push(table.rows[i].cells[0].querySelector("#teacher").textContent)
                selects.push(table.rows[0].cells[j].id)
            }
        }
    }
    document.querySelector('.button.is-link').value = selects
});

for (var i = 1, row; row = table.rows[i]; i++) { // i = 1 instead of 0 to not count the first row aka timings
   // iterate through rows
   // rows would be accessed using the "row" variable assigned in the for loop
   for (var j = 1, col; col = row.cells[j]; j++) { // i = 1 instead of 0 to not count the first col aka names
     // iterate through columns
     // columns would be accessed using the "col" variable assigned in the for loop
     if (table.rows[i].cells[j].classList.contains('is-blocked')) {
       table.rows[i].cells[j].addEventListener('click', function (event) {
        alrBooked(this)
       })
     } else {
        table.rows[i].cells[j].addEventListener('click', function (event) {
          bookSlot(this)
        })
       }
   }
}

function bookSlot(tableCell) {
    // tableCell.parentNode.rowIndex - row num of particular cell,tableCell.cellIndex - col num of particular cell
    // see "https://stackoverflow.com/questions/3400628/how-can-i-get-the-position-of-a-cell-in-a-table-using-javascript/3400673#3400673"
    for (var i = 1; i < table.rows.length; i++) { // go through all rows except first
      // if other cells in same col except itself is booked - so that can still cancel a booked slot
      if (table.rows[i].cells[tableCell.cellIndex].classList.contains('is-booked') && i != tableCell.parentNode.rowIndex) {
        bookConflict(this)
        return;
      }
    }
    tableCell.classList.toggle('is-booked');
}

function alrBooked(tableCell) {
    alert("Slot already booked.");
}

function bookConflict(tableCell) {
    alert("Cannot book multiple slots at once.");
}

