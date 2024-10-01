package com.alanb.test.controller.request

data class AddBookmarkRequest(
    val name: String,
    val url: String,
    val categoryIds: List<String>,
)
