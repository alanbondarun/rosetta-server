package com.alanb.test.business

import com.alanb.test.controller.request.AddCategoryRequest
import com.alanb.test.controller.response.CategoryResponse
import com.alanb.test.controller.response.DeleteCategoryResponse
import com.alanb.test.entity.Category
import com.alanb.test.repository.CategoryRepository
import org.springframework.stereotype.Service
import java.util.UUID

@Service
class CategoryService(
    private val categoryRepository: CategoryRepository,
) {
    fun getCategories(): List<CategoryResponse> {
        return categoryRepository.findAll()
            .map { category ->
                CategoryResponse(
                    id = category.id.toString(),
                    name = category.name,
                )
            }
    }

    fun create(body: AddCategoryRequest): CategoryResponse {
        val newCategory =
            categoryRepository.save(
                Category(
                    name = body.name,
                ),
            )

        return CategoryResponse(
            id = newCategory.id.toString(),
            name = newCategory.name,
        )
    }

    fun delete(categoryId: String): DeleteCategoryResponse {
        val categoryUUID = UUID.fromString(categoryId)
        val categoryExists = categoryRepository.existsById(categoryUUID)
        if (categoryExists) {
            categoryRepository.deleteById(categoryUUID)
        }

        return DeleteCategoryResponse(isDeleted = categoryExists)
    }
}
