/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let totalArr = nums1.concat(nums2);
    totalArr = totalArr.sort(function (a, b) {return a - b});

    const index = totalArr.length / 2;
    if (totalArr.length % 2 === 0) {
        return (totalArr[index - 1] + totalArr[index]) / 2;
    } else {
        return totalArr[Math.floor(index)];
    }
};