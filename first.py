'''def middle(num1,num2):
 #   num1.extend(num2)
  #  num1.sort()
  #  l=len(num1)
  #  if l%2==1:
   #     return num1[l//2]
  #  else:
       return(num1[l//2-1]+num1[l//2])/2'''
def middle(nums1, nums2):
    m, n = len(nums1), len(nums2)
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m
    left1, right1 = 0, m
    while left1 <= right1:
        i = (left1 + right1) // 2
        j = (m + n + 1) // 2 - i
        if i > 0 and j < n and nums1[i - 1] > nums2[j]:
            right1 = i - 1
        elif i < m and j > 0 and nums2[j - 1] > nums1[i]:
            left1 = i + 1
        else:
            if i == 0:
                max_left = nums2[j - 1]
            elif j == 0:
                max_left = nums1[i - 1]
            else:
                max_left = max(nums1[i - 1], nums2[j - 1])
            if (m + n) % 2 == 1:
                return max_left
            if i == m:
                min_right = nums2[j]
            elif j == n:
                min_right = nums1[i]
            else:
                min_right = min(nums1[i], nums2[j])
            return (max_left + min_right) / 2

num1=[1,2]
num2=[3]
print(middle(num1,num2))
