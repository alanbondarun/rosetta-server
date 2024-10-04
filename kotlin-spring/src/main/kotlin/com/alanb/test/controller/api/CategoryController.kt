package com.alanb.test.controller.api

import com.alanb.test.business.CategoryService
import com.alanb.test.controller.request.AddCategoryRequest
import org.springframework.web.bind.annotation.DeleteMapping
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/category")
class CategoryController(
    private val categoryService: CategoryService,
) {
    @GetMapping("")
    fun getCategories(
        @RequestParam(required = false) name: String?,
    ) = categoryService.getCategories(name)

    @PostMapping("")
    fun create(
        @RequestBody body: AddCategoryRequest,
    ) = categoryService.create(body)

    @DeleteMapping("/{categoryId}")
    fun delete(
        @PathVariable categoryId: String,
    ) = categoryService.delete(categoryId)
}
