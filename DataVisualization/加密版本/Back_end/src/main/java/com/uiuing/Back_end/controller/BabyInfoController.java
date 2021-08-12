/*
 * @Author        : uiuing
 * @Date          : 2021-05-18 14:03:07
 * @LastEditTime  : 2021-05-22 19:00:04
 * @LastEditors   : uiuing
 * @Description   : 数据控制
 * @FilePath      : /Back_end/src/main/java/com/uiuing/Back_end/controller/BabyInfoController.java
 * ©️ uiuing.com
 */

package com.uiuing.Back_end.controller;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import javax.annotation.Resource;

import com.alibaba.fastjson.JSON;
import com.uiuing.Back_end.dao.mpDao;

import com.uiuing.Back_end.entity.mp;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@CrossOrigin
public class BabyInfoController {
    @Resource
    mpDao mpDao;

    private boolean flag_pb = false;
    private boolean flag_missing = false;

    /**
     * @description : 初始化
     * @param {int} address_id
     * @return {*}
     */
    @CrossOrigin
    @RequestMapping(value = "/find/start_calculating", method = RequestMethod.POST)
    @ResponseBody
    public String start_calculating(@RequestBody String address_ids) {
        int address_id = Integer.valueOf(address_ids);
        return JSON.toJSONString(Get_approximate_value(address_id), true);
    }

    /**
     * @description : 开始计算
     * @param {int} address_id
     * @return {*}
     */
    private List<mp> Get_approximate_value(int address_id) {

        List<mp> all = new ArrayList<mp>();

        int Pb_size = 0, Mi_size = 0;

        int i = 1;
        while (i != 1000000 && all.size() < 6) {
            String qu_str = String.valueOf(address_id / i) + "%";
            int ram_size[] = size_staf(Pb_size, Mi_size);
            Pb_size = ram_size[0];
            Mi_size = ram_size[1];
            List<mp> ram_pb = MapPb(qu_str, Pb_size);
            List<mp> ram_mi = MapMi(qu_str, Mi_size);
            if (ram_pb != null) {
                all.addAll(ram_pb);
            }
            if (ram_mi != null) {
                all.addAll(ram_mi);
            }
            List<mp> RAM_all = Remove_duplicate_information(all);
            all.clear();
            all.addAll(RAM_all);
            RAM_all.clear();
            i *= 100;
        }

        if (all.size() < 6) {
            all.addAll(add_all("%4", 6 - all.size()));
        }
        Collections.shuffle(all);
        return all;
    }

    /**
     * @description : 判断执行器
     * @param {*}
     * @return {*}
     */
    private int[] size_staf(int A, int B) {
        return flag_pb && flag_missing ? new int[] { 3, 3 } : new int[] { 3 - A, 3 - B };
    }

    /**
     * @description : 根据最近单位获取失踪儿童信息
     * @param {String} qu_str
     * @param {int}    size
     * @return {*}
     */
    private List<mp> MapMi(String qu_str, int size) {
        List<mp> Return = add_all(qu_str, size);
        if (Return == null) {
            return null;
        } else if (Return.size() < 3) {
            flag_missing = false;
        }
        return Return;
    }

    /**
     * @description : 根据概率获取失踪儿童信息
     * @param {String} qu_str
     * @param {int}    size
     * @return {*}
     */
    private List<mp> MapPb(String qu_str, int size) {
        List<mp> Ram_in = new ArrayList<mp>();
        List<mp> Ram_out = new ArrayList<mp>();
        Ram_in = mpDao.select_pb(qu_str);
        Collections.shuffle(Ram_in);
        if (Ram_in.size() == 0)
            return null;
        Double parms = Math.random() / 1000;
        int index = Ram_in.size();
        while (index != 0) {
            --index;
            if (Double.valueOf(Ram_in.get(index).getPb()) > parms) {
                Ram_out = add_all(Ram_in.get(index).getInput(), size);
                if (Ram_out == null) {
                    return null;
                } else if (Ram_out.size() < 3) {
                    flag_pb = false;
                }
                return Ram_out;
            } else if (index == 0) {
                index = Ram_in.size();
                parms = Math.random() / 100000;
            }
        }
        return Ram_out;
    }

    /**
     * @description : 位置对应信息抓取工具
     * @param {String} qu_str
     * @param {int}    size
     * @return {*}
     */
    private List<mp> add_all(String qu_str, int size) {
        List<mp> data_out = new ArrayList<mp>();
        List<mp> data_in = mpDao.select_address_id(qu_str);
        Collections.shuffle(data_in);
        if (data_in.size() == 0)
            return null;
        int index = size;
        if (data_in.size() < size) {
            index = data_in.size();
        }
        while (index != 0) {
            data_out.add(data_in.get(--index));
        }
        return data_out;
    }

    /**
     * @description : 去除重复值
     * @param {List<mp>} data
     * @return {*}
     */
    private List<mp> Remove_duplicate_information(List<mp> data) {
        List<mp> result = new ArrayList<mp>();
        boolean Judgment_criteria = false;
        for (int i = 0; i < data.size(); i++) {
            for (int j = 0; j < result.size(); j++) {
                if (data.get(i).getUrl().equals(result.get(j).getUrl())) {
                    Judgment_criteria = true;
                }
            }
            if (!Judgment_criteria) {
                result.add(data.get(i));
            }
        }
        return result;
    }
    
    /**
     * @description  : 获取开发人数
     * @param         {*}
     * @return        {*}
     */
    @CrossOrigin
    @RequestMapping(value = "/GetDeveloper", method = RequestMethod.POST)
    public String GetDeveloper() {
        return mpDao.select_num().get(0).getNum();
    }

    /**
     * @description  : 添加开发人数
     * @param         {*}
     * @return        {*}
     */
    @CrossOrigin
    @RequestMapping(value = "/AddDeveloper", method = RequestMethod.POST)
    public String AddDeveloper() {
        mpDao.update_num();
        return null;
    }

}
