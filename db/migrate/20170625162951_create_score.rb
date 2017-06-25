class CreateScore < ActiveRecord::Migration[5.1]
  def change
    create_table :scores do |t|
      t.string :player
      t.string :integer
    end
  end
end
