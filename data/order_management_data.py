# coding=utf-8


class OrderManagementData:
    """采购单位发起订购单页面"""
    quantity_selectors = ['name', 'quantity']  # 商品数量
    controlPrice_selectors = ['name', 'controlPrice']  # 意向单价
    grop_buying_selectors = ['css', '#shopObj > tr.level1.mainShop-tr > td:nth-child(14) > div >'
                                    ' div.selectric.checker-color-invalid > b']  # 点击是否团购-选择按钮
    no_grop_buying_selectors = ['css', '#shopObj > tr.level1.mainShop-tr > td:nth-child(14) > div > '
                                       'div.selectric-items > div > ul > li.last']  # 选择是否集团采购=否
    add_plan_selectors = ['name', 'addPlan']  # 添加采购计划按钮
    plan_button_selectors = ['name', 'selectPlan']  # 选择采购计划按钮
    save_plan_selectors = ['id', 'addPlan']  # 保存采购计划按钮
    require_title_selectors = ['id', 'requireTitle']  # 订购单标题
    select_address_selectors = ['name', 'selectAddress']  # 选择地址
    address_quantity_selectors = ['css', '#address-edit-list > table > tbody:nth-child(2) > '
                                         'tr:nth-child(2) > td:nth-child(6) > div > input']  # 选择地址后对应的数量
    submit_selectors = ['id', 'submit-audit-edit']  # 意见审核-提交按钮
    blank_selectors = ['css', '#address-edit-list > table > thead > tr > th:nth-child(6)']  # 选择地址数量后，随意点击页面（数量）
    sure_sumbit_selectors = ['css', 'body > div.modal.modal-dialog.clearfix > div.modal-dialog-message > div > '
                                    'button.btn.btn-minor.submit']  # 确定提交

    """采购单位订购单列表页"""
    # 获取列表页第一行审核按钮
    purchaser_check_selectors = ['css', 'body > div.root-container > div.main-right'
                                        ' > div.bidding-list.js-comp.eve-component > div:nth-child(2) >'
                                        ' div.tab > div > table > tbody > tr:nth-child(1) > td.text-right > a']
    # 获取列表页第一行状态
    status_selectors = ['css', 'body > div.root-container > div.main-right > div.bidding-list.js-comp.eve-component >'
                               ' div:nth-child(2) > div.tab > div > table > tbody > tr:nth-child(1) > td:nth-child(8)']
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
    """采购单位订购审核页面"""
    begin_check_selectors = ['id', 'beginAudit']  # 开始审核按钮
    check_opinion_selectors = ['id', 'checkOpinion']  # 审核意见输入框

    """供应商-订购单管理列表页"""
    confirm_gsy_selectors = ['css', 'body > div.root-container > div.main-right > '
                                    'div.bidding-list.js-comp.eve-component > div:nth-child(2) > div.tab > div > '
                                    'table > tbody > tr:nth-child(1) > td.text-right > a']  # 供应商列表页-第一行-操作按钮
    status_gsy_selectors = ['css', 'body > div.root-container > div.main-right > '
                            'div.bidding-list.js-comp.eve-component > div:nth-child(2) > div.tab > div > '
                            'table > tbody > tr:nth-child(1) > td:nth-child(8)']  # 供应商第一行状态

    """供应商-订购单详情页"""
    accept_gsy_selectors = ['id', 'btn-quote-confirm']  # 供应商-订购单详情页-接受按钮
    accept_ok_gsy_selectors = ['css', 'body > div.modal.confirm-modal.confirm-modal-large > div.modal-footer > '
                                      'button.btn.btn-primary.mr-sm']  # 供应商-订购单详情页-接受按钮-弹窗-同意按钮
    accept_ok_submit_gsy_selectors = ['class', 'submit']  # 供应商-订购单详情页-接受按钮-弹窗-同意按钮-弹窗-确认按钮

    """国和中心列表页"""
    examine_ghzx_selectors = ['css', 'body > div.root-container > div.main-right > '
                                     'div.expert-check-list.js-comp.eve-component > div:nth-child(2) > div > div '
                                     '> table > tbody > tr:nth-child(1) > td:nth-child(9) > a']  # 第一行审核按钮
    examined_status_ghzx_selectors = ['css', 'body > div.root-container > div.main-right > '
                                             'div.expert-check-list.js-comp.eve-component > div:nth-child(2) > '
                                             'div > div > table > tbody > tr:nth-child(1) > td:nth-child(8)']
    """国和中心审核详情页"""
    begin_audit_check_selectors = ['id', 'beginAuditCheck']  # 开始审核按钮
    submit_audits_selectors = ['id', 'submitAudits']  # 提交按钮


