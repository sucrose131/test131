# 配置填写指南 - 详细版

## 📖 使用说明

本文档将指导您如何获取所有需要配置的信息，并告诉您具体在哪个文件的哪一行进行修改。

---

## 🔴 第一部分：数据库配置（最重要）

### 步骤1: 连接数据库

使用以下工具之一连接数据库：
- **Navicat** (推荐)
- **phpMyAdmin**
- **MySQL Workbench**
- **命令行**: `mysql -h 47.112.209.216 -P 13306 -u root -p`

连接信息（已在 `config/global_cfg.py` 中配置）：
```
主机: 47.112.209.216
端口: 13306
数据库: hshome
用户名: root
密码: hsjt1901
```

---

### 步骤2: 查看所有表名

在数据库中执行以下SQL：

```sql
-- 查看所有表
SHOW TABLES;
```

**您需要找到的表**：
1. 验证码表（存储短信验证码）
2. 用户表（存储用户信息）
3. 身份表（存储用户身份信息）
4. 订单表（存储订单信息）
5. 订单权益表（存储订单包含的权益）
6. 产品表（存储产品信息）
7. 用户权益表（存储用户已获得的权益）

**常见表名示例**：
- 验证码表: `verification_codes`, `sms_codes`, `verify_codes`, `captcha`
- 用户表: `users`, `user`, `members`, `accounts`
- 身份表: `user_identities`, `identities`, `user_profiles`, `profiles`
- 订单表: `orders`, `order`, `trade_orders`
- 订单权益表: `order_benefits`, `order_rights`, `order_products`
- 产品表: `products`, `goods`, `items`
- 用户权益表: `user_benefits`, `user_rights`, `user_products`

---

### 步骤3: 查看每个表的结构

对每个表执行：

```sql
DESCRIBE 表名;
-- 或
SHOW COLUMNS FROM 表名;
```

**记录以下信息**：

#### A. 验证码表结构
```sql
DESCRIBE verification_codes;  -- 替换为实际的表名
```

需要记录的字段：
- □ 手机号字段名: _______________ (例如: phone, mobile, telephone)
- □ 验证码字段名: _______________ (例如: code, verify_code, captcha)
- □ 创建时间字段名: _______________ (例如: created_at, create_time, add_time)

**修改位置**: `common/database_helper.py` 第68-75行

```python
# 原代码
sql = """
    SELECT code, created_at 
    FROM verification_codes 
    WHERE phone = %s 
    ORDER BY created_at DESC 
    LIMIT 1
"""

# 修改为（示例）
sql = """
    SELECT verify_code, create_time  # ← 改为实际字段名
    FROM sms_codes                    # ← 改为实际表名
    WHERE mobile = %s                 # ← 改为实际字段名
    ORDER BY create_time DESC         # ← 改为实际字段名
    LIMIT 1
"""
```

---

#### B. 用户表结构
```sql
DESCRIBE users;  -- 替换为实际的表名
```

需要记录的字段：
- □ 用户ID字段名: _______________ (例如: id, user_id, uid)
- □ 手机号字段名: _______________ (例如: phone, mobile, telephone)
- □ 密码字段名: _______________ (例如: password, pwd, user_password)

**修改位置**: `common/database_helper.py` 第97行

```python
# 原代码
sql = "SELECT * FROM users WHERE phone = %s"

# 修改为（示例）
sql = "SELECT * FROM members WHERE mobile = %s"  # ← 改为实际表名和字段名
```

---

#### C. 身份表结构
```sql
DESCRIBE user_identities;  -- 替换为实际的表名
```

需要记录的字段：
- □ 身份表名: _______________
- □ 用户ID字段名: _______________ (外键，关联用户表)
- □ 身份字段名: _______________ (例如: identity_type, identity, level, user_type)
- □ 身份的可能值: _______________ (例如: "普通会员", "vip", "gold")

**修改位置1**: `common/database_helper.py` 第120-126行

```python
# 原代码
sql = """
    SELECT ui.*, u.phone 
    FROM user_identities ui
    LEFT JOIN users u ON ui.user_id = u.id
    WHERE ui.user_id = %s
"""

# 修改为（示例）
sql = """
    SELECT ui.*, u.mobile 
    FROM profiles ui              # ← 改为实际表名
    LEFT JOIN members u ON ui.uid = u.id  # ← 改为实际字段名
    WHERE ui.uid = %s             # ← 改为实际字段名
"""
```

**修改位置2**: `common/database_helper.py` 第147行

```python
# 原代码
actual_identity = identity_info.get('identity_type') or identity_info.get('identity')

# 修改为（示例）
actual_identity = identity_info.get('level') or identity_info.get('user_type')
# ↑ 改为实际的身份字段名
```

**修改位置3**: `testcase/test_register_and_order.py` 第178行

```python
# 原代码
expected_identity = "普通会员"

# 修改为（根据实际业务）
expected_identity = "normal"  # 或 "vip", "gold", "member" 等
# ↑ 改为新注册用户的默认身份值
```

---

#### D. 订单表结构
```sql
DESCRIBE orders;  -- 替换为实际的表名
```

需要记录的字段：
- □ 订单表名: _______________
- □ 订单ID字段名: _______________ (例如: id, order_id, order_no)
- □ 用户ID字段名: _______________ (例如: user_id, uid, customer_id)
- □ 订单状态字段名: _______________ (例如: status, order_status, state)
- □ 订单金额字段名: _______________ (例如: amount, total_amount, price, total)
- □ 发货时间字段名: _______________ (例如: ship_time, delivery_time, shipped_at)
- □ 已发货的状态值: _______________ (例如: 2, 'shipped', 'delivered')

**如何找到已发货的状态值**：

```sql
-- 方法1: 查看已有的已发货订单
SELECT DISTINCT status FROM orders WHERE status IS NOT NULL LIMIT 10;

-- 方法2: 查看订单状态的枚举定义（如果有状态字典表）
SELECT * FROM order_statuses;  -- 或其他状态表

-- 方法3: 手动下一个订单，等待自动发货后查看
SELECT id, status, ship_time FROM orders ORDER BY id DESC LIMIT 1;
```

**修改位置**: `testcase/test_register_and_order.py` 第147-165行

```python
# 断言2: 验证订单属于当前用户
order_user_id = order_info.get('user_id')  # ← 第148行，改为实际字段名

# 断言3: 验证订单状态为已发货
order_status = order_info.get('status')  # ← 第152行，改为实际字段名
self.assertIn(order_status, [2, 'shipped', '已发货'], ...)  # ← 第153行，改为实际状态值

# 断言4: 验证订单金额正确
order_amount = order_info.get('amount') or order_info.get('total_amount')  
# ↑ 第158行，改为实际字段名

# 断言5: 验证发货时间存在
ship_time = order_info.get('ship_time') or order_info.get('delivery_time')
# ↑ 第164行，改为实际字段名
```

---

#### E. 订单权益表和产品表结构

```sql
DESCRIBE order_benefits;  -- 替换为实际的表名
DESCRIBE products;        -- 替换为实际的表名
```

需要记录的字段：
- □ 订单权益表名: _______________
- □ 产品表名: _______________
- □ 订单ID字段名（权益表中）: _______________ (例如: order_id, oid)
- □ 产品ID字段名（权益表中）: _______________ (例如: product_id, goods_id)
- □ 产品名称字段名（产品表中）: _______________ (例如: name, product_name, title)
- □ 权益类型字段名（产品表中）: _______________ (例如: benefit_type, type, category)

**修改位置**: `common/database_helper.py` 第168-173行

```python
# 原代码
sql = """
    SELECT ob.*, p.name as product_name, p.benefit_type 
    FROM order_benefits ob
    LEFT JOIN products p ON ob.product_id = p.id
    WHERE ob.order_id = %s
"""

# 修改为（示例）
sql = """
    SELECT op.*, g.title as product_name, g.type as benefit_type 
    FROM order_products op          # ← 改为实际表名
    LEFT JOIN goods g ON op.goods_id = g.id  # ← 改为实际表名和字段名
    WHERE op.oid = %s               # ← 改为实际字段名
"""
```

---

#### F. 用户权益表结构

```sql
DESCRIBE user_benefits;  -- 替换为实际的表名
```

需要记录的字段：
- □ 用户权益表名: _______________
- □ 用户ID字段名: _______________ (例如: user_id, uid)
- □ 产品ID字段名: _______________ (例如: product_id, goods_id)
- □ 状态字段名: _______________ (例如: status, state, is_active)

**修改位置**: `common/database_helper.py` 第188-194行

```python
# 原代码
sql = """
    SELECT ub.*, p.name as product_name, p.benefit_type
    FROM user_benefits ub
    LEFT JOIN products p ON ub.product_id = p.id
    WHERE ub.user_id = %s AND ub.status = 1
"""

# 修改为（示例）
sql = """
    SELECT up.*, g.title as product_name, g.type as benefit_type
    FROM user_products up           # ← 改为实际表名
    LEFT JOIN goods g ON up.goods_id = g.id  # ← 改为实际表名和字段名
    WHERE up.uid = %s AND up.is_active = 1  # ← 改为实际字段名
"""
```

---

## 🟡 第二部分：API接口配置

### 步骤1: 确认充值接口

**方法1: 查看后台管理系统**
1. 登录后台：https://hshome.backend.test.huasubiotech.com/
2. 找到用户管理或充值功能
3. 打开浏览器开发者工具（F12）
4. 切换到Network标签
5. 执行一次充值操作
6. 查看请求的URL和参数

**方法2: 询问开发人员**
直接询问后端开发人员充值接口的详细信息

**需要记录的信息**：
- □ 充值接口完整路径: _______________
- □ 请求方法: GET / POST / PUT
- □ 参数1名称: _______________ (用户ID)
- □ 参数2名称: _______________ (金额)
- □ 成功返回格式: _______________ (例如: {"code": 200, "message": "success"})
- □ 失败返回格式: _______________

**修改位置1**: `config/global_cfg.py` 第38行

```python
# 原代码
BACKEND_RECHARGE_API = "/backend/admin/user/recharge"

# 修改为（示例）
BACKEND_RECHARGE_API = "/api/admin/recharge"  # ← 改为实际接口路径
```

**修改位置2**: `common/api_helper.py` 第80-83行

```python
# 原代码
params = {
    'user_id': user_id,
    'amount': amount
}

# 修改为（示例）
params = {
    'uid': user_id,      # ← 改为实际参数名
    'money': amount      # ← 改为实际参数名
}
```

**修改位置3**: `common/api_helper.py` 第88行

```python
# 原代码
if result.get('code') == 200 or result.get('success'):

# 修改为（示例）
if result.get('status') == 'ok' or result.get('errno') == 0:
# ↑ 改为实际的成功判断条件
```

---

## 🟢 第三部分：前端元素定位器

### 步骤1: 打开前台网站

访问：https://hshome.h5.test.huasubiotech.com/

### 步骤2: 找到注册入口

1. 按F12打开开发者工具
2. 点击左上角的元素选择工具（或按Ctrl+Shift+C）
3. 点击页面上的"注册"按钮
4. 查看右侧Elements面板中的HTML代码

**示例HTML**：
```html
<button class="register-btn" id="regBtn">注册</button>
```

**编写定位器**：
```python
# 方式1: 使用class
REGISTER_BUTTON = (By.CLASS_NAME, "register-btn")

# 方式2: 使用id
REGISTER_BUTTON = (By.ID, "regBtn")

# 方式3: 使用XPath
REGISTER_BUTTON = (By.XPATH, "//button[@class='register-btn']")

# 方式4: 使用文本
REGISTER_BUTTON = (By.XPATH, "//button[text()='注册']")
```

**修改位置**: `locator/frontend_register_locator.py` 第8行

---

### 步骤3: 找到注册表单元素

点击注册后，对每个输入框重复上述步骤：

#### A. 手机号输入框
```python
# 示例HTML
<input type="tel" name="phone" placeholder="请输入手机号">

# 定位器
PHONE_INPUT = (By.NAME, "phone")
# 或
PHONE_INPUT = (By.XPATH, "//input[@placeholder='请输入手机号']")
```

**修改位置**: `locator/frontend_register_locator.py` 第11行

---

#### B. 验证码输入框
```python
# 示例HTML
<input type="text" name="code" placeholder="请输入验证码">

# 定位器
VERIFICATION_CODE_INPUT = (By.NAME, "code")
```

**修改位置**: `locator/frontend_register_locator.py` 第12行

---

#### C. 密码输入框
```python
# 示例HTML
<input type="password" name="password" placeholder="请输入密码">

# 定位器
PASSWORD_INPUT = (By.NAME, "password")
```

**修改位置**: `locator/frontend_register_locator.py` 第13行

---

#### D. 提交按钮
```python
# 示例HTML
<button type="submit" class="submit-btn">立即注册</button>

# 定位器
SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.submit-btn")
```

**修改位置**: `locator/frontend_register_locator.py` 第20行

---

#### E. 成功提示
```python
# 示例HTML
<div class="success-message">注册成功</div>

# 定位器
SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".success-message")
```

**修改位置**: `locator/frontend_register_locator.py` 第23行

---

## 📊 第四部分：等待时间调整

### 步骤1: 手动测试计时

手动走一遍完整流程，记录每个步骤的时间：

1. □ 验证码生成时间: ___ 秒
2. □ 注册处理时间: ___ 秒
3. □ 订单创建时间: ___ 秒
4. □ 自动发货时间: ___ 秒

### 步骤2: 设置等待时间

**修改位置**: `testcase/test_register_and_order.py`

```python
# 第52行: 验证码等待
time.sleep(2)  # 改为实际时间的1.5倍

# 第130行: 订单创建等待
time.sleep(3)  # 改为实际时间的1.5倍

# 第139行: 自动发货等待
time.sleep(5)  # 改为实际时间的1.5倍
```

---

## ✅ 配置完成检查清单

复制以下清单，逐项打勾：

### 数据库配置
- [ ] 验证码表名已修改 (`database_helper.py` 第70行)
- [ ] 验证码字段名已修改 (`database_helper.py` 第69行)
- [ ] 用户表名已修改 (`database_helper.py` 第97行)
- [ ] 用户ID字段名已确认
- [ ] 身份表名已修改 (`database_helper.py` 第122行)
- [ ] 身份字段名已修改 (`database_helper.py` 第147行)
- [ ] 订单表名已确认
- [ ] 订单状态值已修改 (`test_register_and_order.py` 第153行)
- [ ] 订单金额字段名已修改 (`test_register_and_order.py` 第158行)
- [ ] 发货时间字段名已修改 (`test_register_and_order.py` 第164行)
- [ ] 订单权益表名已修改 (`database_helper.py` 第170行)
- [ ] 产品表名已修改 (`database_helper.py` 第171行)
- [ ] 用户权益表名已修改 (`database_helper.py` 第190行)
- [ ] 预期身份值已修改 (`test_register_and_order.py` 第178行)

### API配置
- [ ] 充值接口路径已修改 (`global_cfg.py` 第38行)
- [ ] 充值参数名已修改 (`api_helper.py` 第81-82行)
- [ ] API成功判断条件已修改 (`api_helper.py` 第88行)

### 前端定位器
- [ ] 注册按钮定位器已修改 (`frontend_register_locator.py` 第8行)
- [ ] 手机号输入框定位器已修改 (`frontend_register_locator.py` 第11行)
- [ ] 验证码输入框定位器已修改 (`frontend_register_locator.py` 第12行)
- [ ] 密码输入框定位器已修改 (`frontend_register_locator.py` 第13行)
- [ ] 提交按钮定位器已修改 (`frontend_register_locator.py` 第20行)
- [ ] 成功提示定位器已修改 (`frontend_register_locator.py` 第23行)

### 等待时间
- [ ] 验证码等待时间已调整 (`test_register_and_order.py` 第52行)
- [ ] 订单创建等待时间已调整 (`test_register_and_order.py` 第130行)
- [ ] 自动发货等待时间已调整 (`test_register_and_order.py` 第139行)

---

## 🚀 测试验证

完成所有配置后：

```bash
# 运行测试
python run.py
```

**如果测试失败**：
1. 查看 `log/` 目录下的日志文件
2. 查看 `img/` 目录下的截图
3. 根据错误信息继续调整配置

**常见错误及解决**：
- "未找到手机号 XXX 的验证码" → 检查验证码表名和字段名
- "元素定位失败" → 检查定位器是否正确
- "充值失败" → 检查充值接口配置
- "订单状态不正确" → 检查订单状态值

---

## 💡 快速查询表

| 配置项 | 文件 | 行号 | SQL查询获取 |
|--------|------|------|-------------|
| 验证码表名 | database_helper.py | 70 | `SHOW TABLES LIKE '%code%';` |
| 用户表名 | database_helper.py | 97 | `SHOW TABLES LIKE '%user%';` |
| 身份表名 | database_helper.py | 122 | `SHOW TABLES LIKE '%identity%' OR '%profile%';` |
| 订单表名 | test_register_and_order.py | 147 | `SHOW TABLES LIKE '%order%';` |
| 订单状态值 | test_register_and_order.py | 153 | `SELECT DISTINCT status FROM orders;` |
| 产品表名 | database_helper.py | 171 | `SHOW TABLES LIKE '%product%' OR '%goods%';` |

---

**祝您配置顺利！如有问题，请查看日志文件获取详细错误信息。**
