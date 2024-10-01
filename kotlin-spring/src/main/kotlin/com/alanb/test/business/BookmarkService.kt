package com.alanb.test.business

import com.alanb.test.controller.request.AddBookmarkRequest
import com.alanb.test.controller.response.BookmarkResponse
import com.alanb.test.controller.response.DeleteBookmarkResponse
import com.alanb.test.entity.Bookmark
import com.alanb.test.entity.Category
import com.alanb.test.repository.BookmarkRepository
import org.springframework.stereotype.Service
import java.util.UUID

@Service
class BookmarkService(
    private val bookmarkRepository: BookmarkRepository,
) {
    fun getBookmarks(): List<BookmarkResponse> {
        return bookmarkRepository.findAll()
            .map { BookmarkResponse.from(it) }
    }

    fun create(body: AddBookmarkRequest): BookmarkResponse {
        val newBookmark =
            bookmarkRepository.save(
                Bookmark(
                    name = body.name,
                    url = body.url,
                    categories =
                        body.categoryIds
                            .map { Category(id = UUID.fromString(it)) }
                            .toMutableSet(),
                ),
            )

        return BookmarkResponse.from(newBookmark)
    }

    fun delete(bookmarkId: String): DeleteBookmarkResponse {
        val bookmarkUUID = UUID.fromString(bookmarkId)
        val bookmarkExists = bookmarkRepository.existsById(bookmarkUUID)
        if (bookmarkExists) {
            bookmarkRepository.deleteById(bookmarkUUID)
        }

        return DeleteBookmarkResponse(isDeleted = bookmarkExists)
    }
}
