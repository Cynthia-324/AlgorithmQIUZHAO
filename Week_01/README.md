## Week 1总结

### 一、Deque 的member functions总结
所用语言以cpp,python为主，这里总结cpp的Deque常用的member functions

```cpp
#include <iostream> 
#include <deque> 
using namespace std; 
deque<int> mydeque;
mydeque.begin() //Return iterator to beginning 
mydeque.end() // Return iterator to end
mydeque.size() // Return size
mydeque.empty() // Test whether container is empty
mydeque.front() // Access first element
mydeque.back() // Access last element 
mydeque.at(2) //Access element
mydeque.push_back() // Add element at the end
mydeque.push_front() // Insert element at beginning
mydeque.pop_back() // Delete last element 
mydeque.pop_front() // Delete first element
it = mydeque.insert (mydeque.begin()+1,10) //Insert elements
```
[deque——C++](http://www.cplusplus.com/reference/deque/deque/)
[Deque in C++ STL](https://www.geeksforgeeks.org/deque-cpp-stl/)

### 二、分析 Queue 和 Priority Queue 的源码
以cpp语言为例
#### Queue
由于deque可以从首位两端插入或剔除元素，所以只需要对其进行简单的封装就可以分别实现先进先出（FIFO）的stack和先进后出（FILO）的queue。
stack和queue中都有一个deque类型的成员，用做数据存储的容器，然后对deque的部分接口进行简单的封装，例如stack只提供从末端插入和删除的接口以及获取末端元素的接口，而queue则只提供从尾部插入而从头部删除的接口以及获取首位元素的接口。
像这样具有“修改某物接口，形成另一种风貌”的性质的，称为配接器（adapter），因此STL中stack和queue往往不被归类为容器（container），而被归类为容器配接器（container adapter）

```cpp
public:
//型别定义
  typedef typename _Sequence::value_type      value_type;
  typedef typename _Sequence::size_type       size_type;
  typedef          _Sequence                  container_type;
  typedef typename _Sequence::reference       reference;
  typedef typename _Sequence::const_reference const_reference;
protected:
  _Sequence c; //底层容器成员变量
public:
  queue() : c() {} //构造器
  explicit queue(const _Sequence& __c) : c(__c) {}

  bool empty() const { return c.empty(); } //判断队列是否为空，调用底层容器相关成员函数即可
  size_type size() const { return c.size(); } //返回队列大小，const函数
  reference front() { return c.front(); } //访问队列头部元素
  const_reference front() const { return c.front(); } //返回队列头部元素，const函数
  reference back() { return c.back(); } //访问队列尾部元素
  const_reference back() const { return c.back(); } //访问队列尾部元素，const函数
  void push(const value_type& __x) { c.push_back(__x); } //入队操作
  void pop() { c.pop_front(); } //出对操作
};
template <class _Tp, class _Sequence>
bool 
operator==(const queue<_Tp, _Sequence>& __x, const queue<_Tp, _Sequence>& __y) //重载==运算符
{
  return __x.c == __y.c;
}

template <class _Tp, class _Sequence>
bool
operator<(const queue<_Tp, _Sequence>& __x, const queue<_Tp, _Sequence>& __y) //重载<运算符
{
  return __x.c < __y.c;
}
```
#### Priority Queue
priority queue 允许用户以任何次序将元素放入容器内，但取出时一定是从优先权最高的元素开始取，binary max heap（二叉大顶堆）即具有这样的特性。
要实现priority queue的功能，binary search tree（BST）也可以作为其底层机制，但这样的话元素的插入就需要O(logN)的平均复杂度，而且要求元素的大小比较随机，才能使树比较平衡。而binary heap是一种完全二叉树的结构，而且可以使用vector来存储：

```cpp
template <class _Tp, class _Sequence __STL_DEPENDENT_DEFAULT_TMPL(vector<_Tp>),
          class _Compare __STL_DEPENDENT_DEFAULT_TMPL(less<typename _Sequence::value_type>) >
class priority_queue { // in stl_queue.h 文件中
protected:
  _Sequence c; // 使用vector作为数据存储的容器
  _Compare comp;
};
 bool empty() const { return c.empty(); } //判断优先队列是否为空
  size_type size() const { return c.size(); } //返回优先队列大小，const函数
  const_reference top() const { return c.front(); } //访问优先队列头部元素，const函数，即优先级最高元素
  void push(const value_type& __x) { //入队
    __STL_TRY { //实现commit or rollback语意
      c.push_back(__x); //元素加入底层容器
      push_heap(c.begin(), c.end(), comp); //元素调整到二叉堆中
    }
    __STL_UNWIND(c.clear());
  }
  void pop() { //出队
    __STL_TRY { //commit or rollback
      pop_heap(c.begin(), c.end(), comp); //元素调整出二叉堆
      c.pop_back(); //元素弹出容器
    }
    __STL_UNWIND(c.clear());
  }
};
```
另外只需要提供一组heap算法，即元素插入和删除、获取堆顶元素等操作即可。
1. push heap 算法
为了满足完全二叉树的特性，新加入的元素一定要放在vector的最后面；又为了满足max-heap的条件（每个节点的键值不小于其叶子节点的键值），还需要执行上溯过程，将新插入的元素与其父节点进行比较，直到不大于父节点
2. pop heap 算法
对heap进行pop操作就是取顶部的元素，取走后要对heap进行调整，是之满足max-heap的特性。调整的策略是，首先将最末尾的元素放到堆顶，然后进行下溯操作，将对顶元素下移到适当的位置
3. make heap 算法
最后，我们来看看如何从一个初始序列来创建一个heap，有了前面的 adjust_heap ，创建heap也就很简单了，只需要从最后一个非叶子节点开始，不断调用堆调整函数，即可使得整个序列称为一个heap

[深入理解STL源码](http://ibillxia.github.io/blog/2014/07/27/stl-source-insight-3-sequential-containers-4-heap-and-priority-queue/)

创建大顶推

```cpp
// C++ program to show that priority_queue is by 
// default a Max Heap 
#include <bits/stdc++.h> 
using namespace std; 

// Driver code 
int main () 
{ 
	// Creates a max heap 
	priority_queue <int> pq; 
	pq.push(5); 
	pq.push(1); 
	pq.push(10); 
	pq.push(30); 
	pq.push(20); 

	// One by one extract items from max heap 
	while (pq.empty() == false) 
	{ 
		cout << pq.top() << " "; 
		pq.pop(); 
	} 

	return 0; 
} 
```
output
> 30 20 10 5 1

创建小顶堆

```cpp
// C++ program to use priority_queue to implement min heap 
#include <bits/stdc++.h> 
using namespace std; 

// Driver code 
int main () 
{ 
	// Creates a min heap 
	priority_queue <int, vector<int>, greater<int> > pq; 
	pq.push(5); 
	pq.push(1); 
	pq.push(10); 
	pq.push(30); 
	pq.push(20); 

	// One by one extract items from min heap 
	while (pq.empty() == false) 
	{ 
		cout << pq.top() << " "; 
		pq.pop(); 
	} 

	return 0; 
} 
```
output
> 1 5 10 20 30 

