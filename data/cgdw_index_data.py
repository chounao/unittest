# coding=utf-8


class CgdwIndexData:
    """商品详情页"""
    bidding_btn_selectors = ['class', 'js-buy-now']  # 生成竞价单按钮
    initate_btn_selectors = ['class', 'js-buy-direct']  # 生成订购单按钮
    addcart_selector = ['class', 'js-add-cart']  # 加入购物车按钮

    """商品详情页-生成订购单-选择供货商窗口"""
    select_btn_selectors = ['id', 'select2-supIdShow-container']  # 选择供货商下拉框
    select_gys_selectors = ['xpath', '//ul[@role="tree"]/li[contains(text(),"云舒001集团有限公司")]']
    checkcart_button_selector = ['link', '查看购物车']  # 加入购物车成功，弹窗窗口-查看购物车按钮

    """购物车页面"""
    allbtn_selector = ["css", "input[.class='ant-checkbox-input'][type='checkbox']:nth-of-type(1)"]  # 购物车页面-第一个全选按钮
    dealersubmit_selector = ['class', 'js-dealer-submit']  # 购物车页面/订单详情页-点击生成订单按钮-选择供应商下拉框-确实按钮
    shoppingcart_selector = ['id', 'shoppingCart']  # 生成竞价单按钮
