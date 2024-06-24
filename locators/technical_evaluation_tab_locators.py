from selenium.webdriver.common.by import By


assembly_node_label = (By.XPATH, '(//li[@class="treeParentList"]//span[@class="node-label"])')
assembly_list_add_btn = (By.XPATH, '(//div[@id="listContainer"])')
add_view_operation = (By.XPATH, '//button[text()="Add/View Operation"]')

machine_loc = (By.XPATH, '//select[@name="machineId"]')
machine_loc_select = (By.XPATH, '(//select[@name="machineId"]/option)')
process_loc = (By.XPATH, '//select[@name="processId"]')
process_loc_select = (By.XPATH, '(//select[@name="processId"]/option)')
process_unit_loc = (By.XPATH, '//select[@name="devProcessUomId"]')
process_unit_loc_select = (By.XPATH, '(//select[@name="devProcessUomId"]/option)')
ops_source_loc = (By.XPATH, '//select[@name="OperationSource"]')
ops_source_loc_select = (By.XPATH, '(//select[@name="OperationSource"]/option)')
assebly_txt_boxes = (By.XPATH, '//label[contains(text(), "field_name")]/..//input')