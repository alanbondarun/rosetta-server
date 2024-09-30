package com.alanb.test.repository

import com.alanb.test.entity.Category
import org.springframework.data.repository.CrudRepository
import java.util.UUID

interface CategoryRepository : CrudRepository<Category, UUID>
