import { Injectable } from '@nestjs/common';
import { CategoryResponse } from './category.response';
import { InjectRepository } from '@nestjs/typeorm';
import { Category } from './category.entity';
import { Repository } from 'typeorm';

@Injectable()
export class CategoryService {
  constructor(
    @InjectRepository(Category)
    private categoryRepository: Repository<Category>,
  ) {}

  getCategories(): Promise<CategoryResponse[]> {
    return this.categoryRepository.find();
  }
}
