import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Category } from './category/category.entity';
import { CategoryModule } from './category/category.module';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: 'localhost',
      port: 5432,
      username: 'rosetta',
      password: 'g9fKklfPCrRivrqYYMltc48C',
      database: 'postgres',
      entities: [Category],
    }),
    CategoryModule,
  ],
})
export class AppModule {}
