# coding=utf-8


class BiddingOrderManagementData:
    """采购单位发起竞价单详情单页面"""

    quantity_selectors = ['name', 'quantity']  # 商品数量
    controlPrice_selectors = ['name', 'controlPrice']  # 意向单价
    # 点击是否团购-选择按钮
    grop_buying_selectors = ['xpath', '//*[@id="shopObj"]/tr/td[13]/div/div[2]/b']
    no_grop_buying_selectors = ['xpath', '//*[@id="shopObj"]/tr/td[13]/div/div[3]/div/ul/li[3]']  # 选择是否集团采购=否
    add_plan_selectors = ['name', 'addPlan']  # 添加采购计划按钮
    plan_button_selectors = ['name', 'selectPlan']  # 选择采购计划按钮
    save_plan_selectors = ['id', 'addPlan']  # 保存采购计划按钮
    plan_num_selectors = ['name', 'usingQuantity']  # 采购计划使用数量
    require_title_selectors = ['id', 'requireTitle']  # 订购单标题
    bidding_cycle_selectors = ['id', 'timeDifference']  # 竞价周期
    select_address_selectors = ['name', 'selectAddress']  # 选择地址
    address_quantity_selectors = ['css', '#address-edit-list > table > tbody:nth-child(2) > '
                                         'tr:nth-child(2) > td:nth-child(6) > div > input']  # 选择地址后对应的数量
    submit_selectors = ['id', 'submit-audit-edit']  # 意见审核-提交按钮
    blank_selectors = ['css', '#address-edit-list > table > thead > tr > th:nth-child(6)']  # 选择地址数量后，随意点击页面（数量）
    sure_sumbit_selectors = ['css', 'body > div.modal.modal-dialog.clearfix > div.modal-dialog-message > div > '
                                    'button.btn.btn-minor.submit']  # 确定提交
    bargaining_success_selectors = ['class', 'success']  # 议价成功标识
    """采购单位竞价单列表页"""

    # 获取列表页第一行状态
    status_selectors = ['css', 'body > div.root-container > div.main-right > '
                               'div.agreementsupply-checklist.js-comp.eve-component > div:nth-child(2) > div > '
                               'div > table > tbody > tr:nth-child(1) > td:nth-child(11)']
    ghzx_stauts_selectors = ['css', 'body > div.root-container > div.main-right > '
                                    'div.agreementsupply-list.js-comp.eve-component > div:nth-child(2) > div.tab > '
                                    'div > table > tbody > tr:nth-child(1) > td:nth-child(11)']  # 专家结果审核状态
    # 获取第一行操作-竞价单审核按钮
    bidding_check_selectors = ['xpath', '/html/body/div[1]/div[3]/div[2]/div[2]/div/div/table/tbody/tr[1]/td[12]/a[1]']
    # 获取第一行操作-结果确认按钮
    result_selectors = ['xpath', '/html/body/div[1]/div[3]/div[2]/div[2]/div[3]/div/table/tbody/tr[1]/td[12]/a[1]']
    """采购单位确认结果，详情页"""
    selectric_gys_selectors = ['css', 'body > div.root-container > div.main-right > '
                                     'div.purinquiry-information-result.js-comp.eve-component > '
                                     'div.health-affirm-result.common-result.js-comp.eve-component > div > '
                                     'div.panel.toggle-panel > div.panel-body > div > div:nth-child(1) > '
                                     'div:nth-child(2) > div.info-content.col-8 > div > div > div.selectric > p']
    result_submit_selectors = ['id', 'resultSubmitAudit']  # 确认成交结果-提交按钮
    """采购单位竞价单审核详情页"""

    begin_check_selectors = ['id', 'beginAudit']  # 最下方开始审核
    check_opinion_selectors = ['id', 'checkOpinion']  # 审核意见输入框
    accept_ok_submit_cgsw_selectors = ['class', 'submit']  # 采购单位-结果确认-提交按钮-弹窗-确定按钮
    bargaining_selectors = ['id', 'bargaining']  # 申请议价选项
    date_input_selectors = ['class', 'date-input']  # 申请议价-要求回复截止时间
    select_hour_selectors = ['class', 'pika-select-hour']  # 申请议价-要求回复截止时间-小时
    click_hour_selectors = ['xpath', '/html/body/div[2]/div[2]/table/tbody/tr/td[1]/select/option[19]']
    # 申请议价-要求回复截止时间-小时-选择时间18点
    reply_bargainingr_selectors = ['xpath', '/html/body/div[2]/div[2]/table/tbody/tr/td[1]/select/option[19]']
    """供货商报价单列表页"""
    # 第一行操作按钮
    offer_btn_selectors = ['css', 'body > div.root-container > div.main-right > '
                                  'div.supplier-information.js-comp.eve-component > div:nth-child(3) > div > div > '
                                  'table > tbody > tr:nth-child(1) > td:nth-child(10) > a']

    """供货商报价详情页"""

    quote_price_selectors = ['id', 'quotePrice']  # 单价报价输入框
    show_promise_selectors = ['id', 'showPromise']  # 下方报价提交按钮
    create_confirm_selectors = ['id', 'createConfirm']  # 报价后弹窗-报价承诺-确定按钮
    quantitys_selectors = ['id', 'quantity']  # 报价优惠率

    """供货商议价列表"""
    bargaining_status_selectors = ['xpath', '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/'
                                            'div/div/div[1]/div/table/tbody/tr/td[6]']  # 第一行-状态-议价中
    reply_bargaining_selectors = ['xpath', '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/'
                                           'div/div/div[2]/div/div/table/tbody/tr[1]/td/span/a']  # 第一行-操作-回复议价

    """供货商回复议价详情页"""
    bargainprice_selectors = ['id', 'bargainPrice']  # 议价单价
    bargainprice_submit_selectors = ['class', 'ant-btn-primary']  # 回复议价-提交按钮
    # 回复议价-提交-确定按钮
    bargainprice_determin_selectors = ['xpath', '/html/body/div[4]/div/div[2]/div/div[1]/div/div/div[2]/button[2]']

    """国和中心列表页"""
    examine_ghzx_selectors = ['css', 'body > div.root-container > div.main-right > '
                                     'div.expert-check-list.js-comp.eve-component > div:nth-child(2) > div > div '
                                     '> table > tbody > tr:nth-child(1) > td:nth-child(9) > a']  # 操作

    examined_status_ghzx_selectors = ['css', 'body > div.root-container > div.main-right > '
                                             'div.expert-check-list.js-comp.eve-component > div:nth-child(2) > '
                                             'div > div > table > tbody > tr:nth-child(1) > td:nth-child(8)']  # 状态
    """国和中心审核详情页"""
    begin_audit_check_selectors = ['id', 'beginAuditCheck']  # 开始审核按钮
    submit_audits_selectors = ['id', 'submitAudit']  # 提交按钮





    # 获取第一行操作-撤回按钮
    remove_selectors = ['css', 'body > div.root-container > div.main-right > div.bidding-list.js-comp.eve-component > '
                               'div:nth-child(2) > div.tab > div > table > tbody > tr:nth-child(1) > td.text-right >'
                               ' a:nth-child(1)']
    remove_reason_selectors = ['id', 'reason']  # 撤回理由
    # 确定撤回按钮
    confirm_remove_selectors = ['css', '#confirm-context-modal > div.btn.pull-right.btn-primary.repeal-require-sure']
    # 第一行状态
    order_finally_status_cgdw_selectors = ['css', 'body > div.root-container > div.main-right > '
                                                  'div.bidding-list.js-comp.eve-component > div:nth-child(2) > '
                                                  'div.tab > div > table > tbody > tr:nth-child(1) > td:nth-child(8)']








