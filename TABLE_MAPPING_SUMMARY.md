---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: 67306d3932a0f88ea6b30df6d25337a8_5dba62176e2311f1aa625254006c9bbf
    ReservedCode1: Lhc9F52uv5M/xDXSjG2D8n7p8Gdozia7vNF4uBCupukIWCrJvp1sDcBg0ZYnKryXzXMZI7awHM6hgZQQJ6K3FAGU+2G+H39Pv9VvZieHWZ97llRjmo3sm8h/y8woYi6xwmORwC8Qozv26+5KkaNCr7AiR2dL5H07nA6DvmXS7NrM5BCh+V2NUytEll8=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: 67306d3932a0f88ea6b30df6d25337a8_5dba62176e2311f1aa625254006c9bbf
    ReservedCode2: Lhc9F52uv5M/xDXSjG2D8n7p8Gdozia7vNF4uBCupukIWCrJvp1sDcBg0ZYnKryXzXMZI7awHM6hgZQQJ6K3FAGU+2G+H39Pv9VvZieHWZ97llRjmo3sm8h/y8woYi6xwmORwC8Qozv26+5KkaNCr7AiR2dL5H07nA6DvmXS7NrM5BCh+V2NUytEll8=
---

# 表结构对照修改汇总

> 生成日期：2026-06-22  
> 项目路径：`D:\131\cloudtranslationPO`  
> 依据文档：`CONFIG_FILLING_GUIDE.md` + 实际数据库表结构

---

## 修改文件清单

| # | 文件 | 修改处数 |
|---|------|---------|
| 1 | `common/database_helper.py` | 5 |
| 2 | `testcase/test_register_and_order.py` | 5 |

---

## 详细修改记录

### 一、common/database_helper.py

| # | 行号 | 修改类型 | 原值 | 新值 | 说明 |
|---|------|---------|------|------|------|
| 1 | 43 | 表名 | `FROM orders` | `FROM hszj_order` | 订单查询SQL，表名改为实际订单表 |
| 2 | 131 | 字段名 | `WHERE hszj_user.id = %s` | `WHERE hszj_user.uid = %s` | 用户唯一索引改用 uid |
| 3 | 158 | 字段名 | `identity_info.get('identity_type') or identity_info.get('identity')` | `identity_info.get('name') or identity_info.get('level')` | 身份字段名改为 name/level |
| 4 | 182-185 | SQL整体替换 | `FROM order_benefits ob LEFT JOIN products p ON ob.product_id = p.id WHERE ob.order_id = %s` (字段: `p.benefit_type`) | `FROM hszj_order_item oi LEFT JOIN hszj_product p ON oi.product_id = p.id WHERE oi.order_sn = %s` (字段: `p.single_type`) | 订单权益表→订单商品表；产品表更名；关联字段 order_id→order_sn；类型字段 benefit_type→single_type |
| 5 | 206-209 | SQL整体替换 | `FROM user_benefits ub LEFT JOIN products p ON ub.product_id = p.id WHERE ub.user_id = %s AND ub.status = 1` (字段: `p.benefit_type`) | `FROM hszj_user_rights ur LEFT JOIN hszj_product p ON ur.product_id = p.id WHERE ur.user_id = %s` (字段: `p.single_type`; 去掉 `AND status=1`) | 用户权益表更名；产品表更名；去掉status过滤条件；类型字段 benefit_type→single_type |

### 二、testcase/test_register_and_order.py

| # | 行号 | 修改类型 | 原值 | 新值 | 说明 |
|---|------|---------|------|------|------|
| 1 | 153 | 字段名 | `order_info.get('status')` | `order_info.get('order_status')` | 订单状态字段名 |
| 2 | 155 | 状态值 | `[2, 'shipped', '已发货']` | `[4]` | 已发货状态值改为 4 |
| 3 | 160 | 字段名 | `order_info.get('amount') or order_info.get('total_amount')` | `order_info.get('actual_amount') or order_info.get('total_amount')` | 优先使用实际支付金额 |
| 4 | 166 | 字段名 | `order_info.get('ship_time') or order_info.get('delivery_time')` | `order_info.get('shipping_time')` | 发货时间字段名 |
| 5 | 183 | 预期值 | `"普通会员"` | `"个人消费者"` | 新注册用户默认 level=0 |

---

## 表结构对照速查

| 业务概念 | 实际表名 | 关键字段 |
|---------|---------|---------|
| 验证码 | `hszj_user_mobile_code` | `mobile`, `code`, `created_at` |
| 用户 | `hszj_user` | `uid` (唯一索引), `mobile`, `password`, `level_id` |
| 用户等级 | `hszj_user_level` | `id`, `name`, `level` (0-个人消费者, 1-全家福, 2-事业合伙人, 3-创始合伙人) |
| 订单 | `hszj_order` | `order_sn`, `user_id`, `order_status`, `actual_amount`, `total_amount`, `shipping_time` |
| 订单商品 | `hszj_order_item` | `order_sn` (关联订单), `product_id` |
| 产品 | `hszj_product` | `name`, `single_type`, `type` |
| 用户权益 | `hszj_user_rights` | `user_id`, `product_id` (无 status 字段) |

---

## 关联关系

```
hszj_user.level_id  →  hszj_user_level.id
hszj_order_item.order_sn  →  hszj_order.order_sn
hszj_order_item.product_id  →  hszj_product.id
hszj_user_rights.product_id  →  hszj_product.id
```
*（内容由AI生成，仅供参考）*
