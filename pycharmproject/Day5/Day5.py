# 通过class 类名
class Cat:
    # 构造函数 对象创建的时候就自动调用了 似乎无法设置多个构造函数
    def __init__(self,name,age):
        # print("无参构造")1
        self.name=name;
        self.age=age;
    def eat(self):
        print(self.name+"猫吃")
        # print(self.name+"猫吃")

    def run(self):
        print("猫跑")

    def count(self,num):
        try:
            add=num+1
            print("传入%.2f,猫会加1:%d" %(num,add))
        except Exception as e:
            print(e)

tom=Cat("tom",1)
# tom.name="Tom"//不需要构造方法也能设置独有的属性 但是会导致别的实例对象崩溃
tom.count(5)
