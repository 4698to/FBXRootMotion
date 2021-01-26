# 2021.01.24 FBX Rootmotion

基于 FBXSDK-python 的角色动画处理工具，如带位移的走路动作，直接将移动距离做在角色骨架上，那你就可以用这个工具把这个位移转到 root 骨骼上。

直接处理FBX资源，不需要用3ds max 处理资源，这里只是借用 3ds Max2021 的 python 环境。




### 请注意是直接处理 FBX 文件，不是把FBX导入3ds max 再处理。

# 使用步骤：
*   把FBX文件拖拽到 .fbx 框范围中（偷懒不写文件选择列表了）
*   设置你FBX角色的根骨骼名字 和 角色质心骨骼名字 (如果没有根骨骼会跳过处理)
*   设置另保存的路径，默认路径是覆盖保存！
*   设置位移轴向
*   点击确定按钮

![](https://gitee.com/to4698/ND_tools/raw/master/img/001/07-1611579919049.png)

## 其他
*   目前只支持 Yup 轴向的FBX 文件
*   后续考虑加入自动创建 root 功能
*   目前测试正常的是根骨骼无旋转值的资源，有的 unity 资源的根骨骼会有 90的旋转偏移，没测试过能否正常处理，如遇到联系我。
![](https://gitee.com/to4698/ND_tools/raw/master/img/001/53A8223F-8A3A-4257-974D-6F3EA63A54C6.png)

![](https://gitee.com/to4698/ND_tools/raw/master/img/001/53F2EE48-830B-439A-BFEB-4D0F38E5850A.png)

# 安装

*   1. 把你下载到的 FBXRootmotion 文件夹放到 3ds max 如下图的路径中

![](https://gitee.com/to4698/ND_tools/raw/master/img/001/07-1611579391830.png)


*   2. 将 菜单栏Rootmotionui_v1.0_menu.ms 拖拽进 3ds max 中创建 FBXRootmotion 菜单栏

![](https://gitee.com/to4698/ND_tools/raw/master/img/001/07-1611579472379.png)

*   3. 选中 FBXRootmotion 即可打开

![](https://gitee.com/to4698/ND_tools/raw/master/img/001/07-1611579578213.png)

# 下载

链接：https://pan.baidu.com/s/1KRtP5HcvTKLInFQGNg9G0g
提取码：1lqo

-----

E-Mail: 738746223@qq.com

99U : 199505

反馈交流群号：109185941
点击链接加入群聊【天晴工具组】：https://jq.qq.com/?_wv=1027&k=YJSgv3fe

如果觉的工具好用，欢迎捐赠以示支持，让洒家有动力更新啊

![](https://gitee.com/to4698/ND_tools/raw/master/img/1516971249924.jpg)