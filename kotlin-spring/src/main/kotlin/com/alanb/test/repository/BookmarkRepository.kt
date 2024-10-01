package com.alanb.test.repository

import com.alanb.test.entity.Bookmark
import org.springframework.data.repository.CrudRepository
import java.util.UUID

interface BookmarkRepository : CrudRepository<Bookmark, UUID>
