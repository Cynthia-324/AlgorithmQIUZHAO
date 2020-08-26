
# 快速排序

```c++
//C/C++
int random_partition(vector<int>& nums, int l, intr) {
  int random_pivot_index = rand() % (r - l +1) + l;  //随机选择pivot
  int pivot = nums[random_pivot_index];
  swap(nums[random_pivot_index], nums[r]);
  int i = l - 1;
  for (int j=l; j<r; j++) {
    if (nums[j] < pivot) {
      i++;
      swap(nums[i], nums[j]);
    }
  }
  int pivot_index = i + 1;
  swap(nums[pivot_index], nums[r]);
  return pivot_index;
}
void random_quicksort(vector<int>& nums, int l, int r) {
  if (l < r) {
    int pivot_index = random_partition(nums, l, r);
    random_quicksort(nums, l, pivot_index-1);
    random_quicksort(nums, pivot_index+1, r);
  }
}
```
```python
#Python
def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index-1, nums)
    quick_sort(pivot_index+1, end, nums)
    
def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin+1, end+1):
        if nums[i] < pivot:
            mark +=1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark
```
![图片](https://uploader.shimo.im/f/G6nPE2zWpngKXZSM.png!thumbnail)

![图片](https://uploader.shimo.im/f/v5igSvfL4wAtG6GP.png!thumbnail)

# 归并排序

```c++
void mergeSort(vector<int> &nums, int left, int right) {
  if (left >= right) return;
  int mid = left + (right - left) / 2;
  mergeSort(nums, left, mid);
  mergeSort(nums, mid+1, right);
  merge(nums, left, mid, right);
}

void merge(vector<int> &nums, int left, int mid, int right) {
    vector<int> tmp(right-left+1);
    int i = left, j = mid+1, k = 0;
    while (i <= mid && j <= right) {
        tmp[k++] = nums[i] < nums[j] ? nums[i++] : nums[j++];
    }
    while (i <= mid) tmp[k++] = nums[i++];
    while (j <= right) tmp[k++] = nums[j++];
    for (i = left, k = 0; i <= right;) nums[i++] = tmp[k++];
}
```

```python
#Python
def mergesort(nums, left, right):
    if right <= left:
        return
    mid = (left+right) >> 1
    mergesort(nums, left, mid)
    mergesort(nums, mid+1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    temp = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i +=1
        else:
            temp.append(nums[j])
            j +=1
    while i<=mid:
        temp.append(nums[i])
        i +=1
    while j<=right:
        temp.append(nums[j])
        j +=1
    nums[left:right+1] = temp
```
[https://shimo.im/docs/M2xfacKvwzAykhz6/read](https://shimo.im/docs/M2xfacKvwzAykhz6/read)
# 堆排序

```python
#Python
def heapify(parent_index, length, nums):
    temp = nums[parent_index]
    child_index = 2*parent_index+1
    while child_index < length:
        if child_index+1 < length and nums[child_index+1] > nums[child_index]:
            child_index = child_index+1
        if temp > nums[child_index]:
            break
        nums[parent_index] = nums[child_index]
        parent_index = child_index
        child_index = 2*parent_index + 1
    nums[parent_index] = temp



def heapsort(nums):
    for i in range((len(nums)-2)//2, -1, -1):
        heapify(i, len(nums), nums)
    for j in range(len(nums)-1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]
        heapify(0, j, nums)
```
```c++
C/C++

void heapify(vector<int> &array, int length, int i) {
    int left = 2 * i + 1, right = 2 * i + 2;
    int largest = i;

    if (left < length && array[left] > array[largest]) {
        largest = left;
    }
    if (right < length && array[right] > array[largest]) {
        largest = right;
    }

    if (largest != i) {
        int temp = array[i]; array[i] = array[largest]; array[largest] = temp;
        heapify(array, length, largest);
    }

    return ;
}
void heapSort(vector<int> &array) {
    if (array.size() == 0) return ;

    int length = array.size();
    for (int i = length / 2 - 1; i >= 0; i--) 
        heapify(array, length, i);

    for (int i = length - 1; i >= 0; i--) {
        int temp = array[0]; array[0] = array[i]; array[i] = temp;
        heapify(array, i, 0);
    }

    return ;
}
```
或者小顶堆
