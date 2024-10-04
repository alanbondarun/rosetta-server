package com.alanb.test.controller.api

import com.alanb.test.business.BookmarkService
import com.alanb.test.controller.request.AddBookmarkRequest
import org.springframework.web.bind.annotation.DeleteMapping
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/bookmark")
class BookmarkController(
    private val bookmarkService: BookmarkService,
) {
    @GetMapping("")
    fun getBookmarks(
        @RequestParam(required = false) categoryId: String?,
    ) = bookmarkService.getBookmarks(categoryId)

    @PostMapping("")
    fun create(
        @RequestBody body: AddBookmarkRequest,
    ) = bookmarkService.create(body)

    @DeleteMapping("/{bookmarkId}")
    fun delete(
        @PathVariable bookmarkId: String,
    ) = bookmarkService.delete(bookmarkId)
}
