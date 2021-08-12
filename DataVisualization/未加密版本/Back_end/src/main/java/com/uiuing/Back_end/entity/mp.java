/*
 * @Author        : uiuing
 * @Date          : 2021-05-17 21:35:13
 * @LastEditTime  : 2021-05-22 17:57:59
 * @LastEditors   : uiuing
 * @Description   :  table 字段映射
 * @FilePath      : /Back_end/src/main/java/com/uiuing/Back_end/entity/mp.java
 * ©️ uiuing.com
 */

package com.uiuing.Back_end.entity;

public class mp {
    private String name;
    private String sex;
    private String birth;
    private String missing_time;
    private String address;
    private String person;
    private String after;
    private String image;
    private String url;
    private String input;
    private String pb;
    private String address_id;
    private String num;

    public String getInput() {
        return input;
    }

    public String getNum() {
        return num;
    }

    public void setNum(String num) {
        this.num = num;
    }

    public String getAddress_id() {
        return address_id;
    }

    public void setAddress_id(String address_id) {
        this.address_id = address_id;
    }

    public void setInput(String input) {
        this.input = input;
    }

    public String getPb() {
        return pb;
    }

    public void setPb(String pb) {
        this.pb = pb;
    }

    public String getName() {
        return name;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getBirth() {
        return birth;
    }

    public void setBirth(String birth) {
        this.birth = birth;
    }

    public String getMissing_time() {
        return missing_time;
    }

    public void setMissing_time(String missing_time) {
        this.missing_time = missing_time;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPerson() {
        return person;
    }

    public void setPerson(String person) {
        this.person = person;
    }

    public String getAfter() {
        return after;
    }

    public void setAfter(String after) {
        this.after = after;
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

}