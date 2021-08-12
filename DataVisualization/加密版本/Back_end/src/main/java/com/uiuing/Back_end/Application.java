/*
 * @Author        : uiuing
 * @Date          : 2021-05-18 14:18:53
 * @LastEditTime  : 2021-05-20 22:28:05
 * @LastEditors   : uiuing
 * @Description   : 
 * @FilePath      : /Back_end/src/main/java/com/uiuing/Back_end/Application.java
 * ©️ uiuing.com
 */

package com.uiuing.Back_end;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.uiuing.Back_end.dao") // 添加 @Mapper 注解
public class Application {
    public static void main(String[] args) {
        System.out.println("启动 Spring Boot...");
        SpringApplication.run(Application.class, args);
    }
}
