package com.alanb.test.controller.api

import com.alanb.test.business.CategoryService
import com.alanb.test.controller.request.AddCategoryRequest
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/category")
class CategoryController(
    private val categoryService: CategoryService,
) {
    @GetMapping("")
    fun getCategories() =
        categoryService.getCategories()

    @PostMapping("")
    fun createCategory(
        @RequestBody body: AddCategoryRequest
    ) =
        categoryService.create(body)
}
