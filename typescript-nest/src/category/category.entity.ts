import { Column, Entity, PrimaryColumn } from 'typeorm';

@Entity()
export class Category {
  @PrimaryColumn({
    type: 'uuid',
  })
  id: string;

  @Column()
  name: string;
}
