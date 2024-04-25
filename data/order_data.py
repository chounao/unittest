# coding=utf-8


class OrderData:
    # 电子卖场
    mall_selectors = ['class', 'icon-maichang']
    # 疫苗馆首页-搜索框
    search_selectors = ['name', 'q']
    # 疫苗搜索按钮
    vaccine_btn_selectors = ['id', 'search-button']
    # 搜索结果
    goodslink_selectors = ['link', '甲型肝炎灭活疫苗0508']
    # 购物车页面-第一个全选按钮
    # allbtn_selectors = ['xpath', '//input[@class="ant-checkbox-input"]']
    allbtn_selectors = ['xpath', '//input[@class="ant-checkbox-input"]']
    # 购物车页面-全部删除按钮
    batchdeletebtn_selectors = ['xpath', '//div[@class="float-bar-action-del"]/a[text()="删除"]']
    # 购物车页面-确定删除按钮
    surebtn_selectors = ['xpath', '//button[@class="ant-btn ant-btn-primary ant-btn-sm ant-btn-two-chinese-chars"]']
    # 购物车页面-商品名称
    cart_goodsname_selectors = ['link', '甲型肝炎灭活疫苗0508']
    # surebtn_selectors = ['xpath', '//*[contains(text(),"确定")]']
    # 商品详情页-加入购物车按钮
    addcart_selectors = ['xpath', '//*[contains(text(),"加入购物车")]']
    # 加入购物车成功窗口-查看购物车按钮
    checkcart_selectors = ['xpath', '//*[contains(text(),"查看购物车")]']  # 加入购物车成功，弹窗窗口-查看购物车按钮
    # 商品详情页-立即下单按钮
    orderbtn_selectors = ['xpath', '//*[contains(text(),"立即下单")]']
    # 购物车页面-生成预购单按钮
    addinitate_selectors = ['xpath', '//button[@class="ant-btn ant-btn-primary ant-btn-lg" and @type="button"]']
    # 创建预购单页面-发票管理
    invoice_selectors = ['link', '添加发票']
    # 创建预购单页面-选择部门审核人下拉框
    select_placeholder_selectors = ['class', 'select2-selection__placeholder']
    # 部门审核人
    placeholder_selectors = ['xpath', '//li[text()="席胜军"]']
    # 提交按钮
    submit_selectors = ['xpath', '//button[text()="提交"]']
    # 弹窗-确定提交
    sure_selectors = ['class', 'submit']
    # 弹窗-预购单提交成功-确定（关闭）
    close_selectors = ['xpath', '//button[@class="btn btn-minor submit close"]']
    # 关闭采宝
    shrink_selectors = ['class', 'shrink-png']
    # 预购单列表-第一行-操作
    purchaser_check_selectors = ['css', 'div.pur-list-body > table > tbody > '
                                        'tr:nth-child(1) > td:nth-child(7) > a:nth-child(1)']
    # 部门审核-提交审核意见
    check_submit_selectors = ['xpath', '//button[text()="提交审核意见"]']
    # 确定订单页面-确定订单按钮
    submit_order_selectors = ['xpath', '//button[text()="确定订单"]']
    # 订单列表-状态
    order_status_selectors = ['css', 'div.order-form-list-body > table > tbody > tr:nth-child(1) > td:nth-child(7)']
    # 订单列表-操作
    order_operation_selectors = ['css', 'div.order-form-list-body > table > tbody > tr:nth-child(1) > '
                                        'td:nth-child(8)> a:nth-child(1)']
    # 订单列表-操作-再次购买
    buy_again_selectors = ['css', 'div.order-form-list-body > table > tbody > '
                                  'tr:nth-child(1) > td:nth-child(8)> a.js-buy-again']
    # 订单列表-操作(供应商接单后-取消订单)
    order_cancel_selectors = ['css', 'div.order-form-list-body > table > tbody > tr:nth-child(1) >'
                                     ' td:nth-child(8)> a:nth-child(3)']
    # 订单列表-操作
    order_operation_two_selectors = ['css', 'div.order-form-list-body > table > tbody > '
                                            'tr:nth-child(1) > td:nth-child(8)> a.js-order-check']
    # 取消订单窗口-取消理由输入框
    cancel_reason_selectors = ['id', 'js-cancel-reason']
    # 取消订单窗口-确定按钮
    cancel_submit_selectors = ['xpath', '//button[text()="确定"]']
    # 供应商-订单详情页-操作（接单）
    gys_operate_selectors = ['css', 'div.order-form-list-body > table > tbody > tr:nth-child(1)  > td:nth-child(7) > a']
    # 供应商-订单详情页-操作（取消订单）
    gys_cancel_selectors = ['css', 'div.order-form-list-body > table > tbody > tr:nth-child(1)  > '
                                   'td:nth-child(7) > a:nth-child(3)']
    # 供应商-接单-弹窗-确认接单
    gys_requier_selectors = ['xpath', '//button[text()="确认接单"]']
    # 供应商-订单列表-状态
    gys_status_selectors = ['css', 'div.order-form-list-body > table > tbody > tr:nth-child(1) > td:nth-child(6)']
    # 供应商-订单详情页-发货按钮
    gys_send_goods_selectors = ['css', 'div.order-form-list-body > table > tbody > tr:nth-child(1)  > '
                                       'td:nth-child(7) > a:nth-child(3)']
    # 供应商发货页面-发货仓库-请选择
    gys_warehouse_selectors = ['class', 'selectric-js-all-select-warehouse']
    # 供应商发货页面-下拉框-默认仓库
    gys_default_warehouse_selectors = ['xpath', '//li[contains(text(),"默认仓库")]']
    # 供应商发货页面-选择商品
    gys_check_goods_selectors = ['xpath', '//*[@type="checkbox"]']
    # 供应商发货页面 - 添加批号
    gys_add_batch_selectors = ['xpath', '//*[contains(text(),"添加批号")]']
    # 供应商发货页面 -添加批号弹窗-请选择
    gys_select_selectors = ['class', 'select2-selection__rendered']
    # 供应商发货页面 -选择批号
    gys_select_batch_selectors = ['css', 'ul.select2-results__options > li:nth-child(2)']
    # 供应商发货页面 -发货数量
    gys_goodscount_selectors = ['name', 'goodsCount']
    # 供应商发货页面 -添加批号-确定按钮
    gys_batch_require_selectors = ['xpath', '//button[text()="确定"]']
    # 供应商发货页面 -运单号
    gys_shipmentno_selectors = ['class', 'js-shipmentNo']
    # 供应商发货页面 - 确认发货
    gys_items_submit_selectors = ['xpath', '//button[text()="确认发货"]']
    # 采购单位 - 订单详情 - 确认收货
    revice_goods_selectors = ['link', '确认收货']
    # 采购单位 - 订单详情 - 确认收货-弹窗 -温度验收完成
    temperature_check_selectors = ['name', 'hasChecked']
    # 采购单位 - 订单详情 - 确认收货-弹窗 -确认收货
    sure_revice_selectors = ['xpath', '//button[text()="确认收货"]']
    # 供应商-取消订单弹窗-备注
    gys_cancel_reason_selectors = ['id', 'js-cancel-reason']
    # 供应商-取消订单弹窗-确定按钮
    gys_cancel_sure_selectors = ['xpath', '//button[text()="确定"]']