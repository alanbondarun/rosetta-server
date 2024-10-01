package com.alanb.test.controller.response

import com.alanb.test.entity.Bookmark

data class BookmarkResponse(
    val id: String,
    val name: String,
    val url: String,
    val categories: List<CategoryResponse>,
) {
    companion object {
        fun from(bookmark: Bookmark) =
            with(bookmark) {
                BookmarkResponse(
                    id = id.toString(),
                    name = name,
                    url = url,
                    categories =
                        categories.map { categories ->
                            CategoryResponse(
                                id = categories.id.toString(),
                                name = categories.name,
                            )
                        },
                )
            }
    }
}
