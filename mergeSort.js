const nums = [2, 31234, 123, 1];

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
  let mid = Math.floor((left + right) / 2);
  mergeSort(arr, left, mid);
  mergeSort(arr, mid + 1, right);
  merge(arr, left, mid, right);
  return arr;
}

console.log(mergeSort(nums, 0, nums.length - 1));
