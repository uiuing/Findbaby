/*
 * @Author        : uiuing
 * @Date          : 2021-05-17 21:49:07
 * @LastEditTime  : 2021-05-22 18:18:50
 * @LastEditors   : uiuing
 * @Description   : 查询接口
 * @FilePath      : /Back_end/src/main/java/com/uiuing/Back_end/dao/mpDao.java
 * ©️ uiuing.com
 */

package com.uiuing.Back_end.dao;

import com.uiuing.Back_end.entity.mp;

import java.util.List;

public interface mpDao {
    /**
     * @description : 查询地址数据
     * @param {String} address_id
     * @return {*} List<mp>
     */
    public List<mp> select_address_id(String address_id);

       /**
     * @description : 查询概率数据
     * @param {String} outs
     * @return {*} List<mp>
     */
    public List<mp> select_pb(String outs);
    
      /**
     * @description : 更新开发者数量
     * @param {String} num
     * @return {*} List<mp>
     */
    public List<mp> update_num();

    /**
     * @description : 查询开发者数量
     * @param {String} num
     * @return {*} List<mp>
     */
    public List<mp> select_num();
}