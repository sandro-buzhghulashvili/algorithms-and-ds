const nums = [2, 31234, 123, 1];

//[1,3]

function merge(arr, L, M, R) {
  let left = arr.slice(L, M + 1);
  let right = arr.slice(M + 1, R + 1);
  let i = L,
    j = 0,
    k = 0;

  while (j < left.length && k < right.length) {
    if (left[j] <= right[k]) {
      arr[i] = left[j];
      j += 1;
    } else {
      arr[i] = right[k];
      k += 1;
    }
    i += 1;
  }
  while (j < left.length) {
    arr[i] = left[j];
    j += 1;
    i += 1;
  }
  while (k < right.length) {
    arr[i] = right[k];

    k += 1;
    i += 1;
  }
}

function mergeSort(arr, left, right) {
  if (left === right) return arr;
  let mid = Math.floor((left + right) / 2); //
  mergeSort(arr, left, mid); // [0]
  mergeSort(arr, mid + 1, right); // [1]
  merge(arr, left, mid, right);
  return arr;
}

// [2,4,2,1]

console.log(mergeSort(nums, 0, nums.length - 1));

// function mergeSortedArrays(arr, left, mid, right) {
//   let leftSide = arr.slice(left, mid + 1); // [7, 9]
//   let rightSide = arr.slice(mid + 1, right + 1); // [2, 5]

//   // mergeSortedArrays([7, 9, 2, 5], 0, 1, 3);

//   let pointerOfArr = left; //0 > 1 > 2
//   let pointerOfLeftPart = 0; // Start from the beginning of leftSide
//   let pointerOfRightPart = 0; // Start from the beginning of rightSide > 1 > 2

//   while (
//     pointerOfLeftPart < leftSide.length &&
//     pointerOfRightPart < rightSide.length
//   ) {
//     if (leftSide[pointerOfLeftPart] <= rightSide[pointerOfRightPart]) {
//       arr[pointerOfArr] = leftSide[pointerOfLeftPart];
//       pointerOfLeftPart += 1;
//     } else {
//       arr[pointerOfArr] = rightSide[pointerOfRightPart];
//       pointerOfRightPart += 1;
//     }
//     pointerOfArr += 1;
//   }

//   while (pointerOfLeftPart < leftSide.length) {
//     arr[pointerOfArr] = leftSide[pointerOfLeftPart];
//     pointerOfLeftPart += 1;
//     pointerOfArr += 1;
//   }

//   while (pointerOfRightPart < rightSide.length) {
//     arr[pointerOfArr] = rightSide[pointerOfRightPart];
//     pointerOfRightPart += 1;
//     pointerOfArr += 1;
//   }

//   console.log(arr);
// }

// mergeSortedArrays([7, 9, 2, 5], 0, 1, 3);
