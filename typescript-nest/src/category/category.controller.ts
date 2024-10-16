import { Controller, Get } from '@nestjs/common';
import { CategoryService } from './category.service';
import { CategoryResponse } from './category.response';

@Controller('/category')
export class CategoryController {
  constructor(private readonly categoryService: CategoryService) {}

  @Get()
  getCategories(): Promise<CategoryResponse[]> {
    return this.categoryService.getCategories();
  }
}
