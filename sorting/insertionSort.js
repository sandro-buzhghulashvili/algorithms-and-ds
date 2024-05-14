const array = [3, 1, 5, 12, 2, 232, 12, 23, 3];

function InsertionSort(array) {
  for (i = 1; i < array.length; i++) {
    let key = array[i]; //2
    let j = i - 1; //3 -> 2 -> 1 ->  0
    while (j >= 0 && array[j] > key) {
      array[j + 1] = array[j];
      j -= 1;
    }
    array[j + 1] = key;
  }
  return array;
}
console.log(InsertionSort(arr));
